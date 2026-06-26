import time
from google import genai
from agents.adk_definitions import AgentSystemPrompts

client = genai.Client()

# Helper function to add resilience to our Agents
def call_agent_with_retry(prompt: str, system_instruction: str, model: str = 'gemini-3.5-flash', retries: int = 3):
    for attempt in range(retries):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
                config=genai.types.GenerateContentConfig(system_instruction=system_instruction)
            )
            return response.text
        except Exception as e:
            error_str = str(e)
            if "503" in error_str or "429" in error_str:
                if attempt < retries - 1:
                    time.sleep(2)  # Wait 2 seconds and try again
                    continue
            return f"⚠️ Agent Communication Failure: {error_str}"

def run_legacy_extraction_flow(customer_id: str):
    logs = []
    
    # --- DYNAMIC MOCK LEGACY DB ---
    mock_mainframe_db = {
        "10045892": "10045892KUMAR,R        198504120004589200A R4", # Clean / Medium Risk
        "10045893": "10045893SHARMA,P       199011050000005000C R9", # Closed / High Risk
        "99999999": "99999999JUDGE,TEST     198001010009999900A R1"  # Custom one for the judges
    }
    
    raw_legacy_string = mock_mainframe_db.get(customer_id)
    
    if not raw_legacy_string:
        logs.append(f"⚠️ ERR: Record {customer_id} not found in Mainframe VSAM file.")
        return {"modern_insight": "Record Not Found", "compliance_status": "Halted", "audit_trail": logs}
    # ------------------------------

    logs.append(f"Initiating legacy fetch for {customer_id}...")
    logs.append(f"Mock Data Retrieved: {raw_legacy_string}")
    scout_text = call_agent_with_retry(
        prompt=f"Analyze this raw string: {raw_legacy_string}",
        system_instruction=AgentSystemPrompts.SCOUT,
        model='gemini-3.1-flash-lite'  # <-- Updated to the correct 3.1 version
    )
    if "⚠️" in scout_text: return {"modern_insight": "Extraction Failed", "compliance_status": "Halted", "audit_trail": logs + [scout_text]}
    logs.append(f"Scout Mapping: {scout_text}")

    # 3. Knowledge Bridge translates it
    logs.append("Deploying Knowledge Bridge Agent for tribal rules...")
    bridge_text = call_agent_with_retry(
        prompt=f"Translate this mapped data using your tribal knowledge: {scout_text}",
        system_instruction=AgentSystemPrompts.KNOWLEDGE_BRIDGE,
        model='gemini-3.1-flash-lite'  # <-- Updated to the correct 3.1 version
    )
    if "⚠️" in bridge_text: return {"modern_insight": "Translation Failed", "compliance_status": "Halted", "audit_trail": logs + [bridge_text]}
    
    # 4. Compliance Check
    logs.append("Deploying Compliance Agent...")
    compliance_text = call_agent_with_retry(
        prompt=f"Review this profile for RBI compliance: {bridge_text}",
        system_instruction=AgentSystemPrompts.COMPLIANCE
    )
    logs.append(f"Compliance Gate: {compliance_text}")

    # 5. Output structure
    return {
        "status": "success",
        "customer_id": customer_id,
        "modern_insight": bridge_text,
        "compliance_status": compliance_text,
        "audit_trail": logs
    }