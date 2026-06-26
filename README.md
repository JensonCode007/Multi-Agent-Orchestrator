# 🛡️ LegacyGuard AI Orchestrator

**Bridging 1995 Mainframes with Agentic AI**
*Built for the [Insert Hackathon Name] - Track B*

## 🚨 The Core Problem
**Decades of accumulated process debt in the enterprise sector.**
Most AI pilots fail (95%) not due to model capability, but the inability to safely integrate with ancient mainframes, siloed databases, compliance layers, and the tribal knowledge held by retiring experts. 
* India’s $300B+ IT services industry is at risk of losing its global edge unless it masters legacy integration in the agentic AI era.
* We don’t have an AI problem. We have a *Legacy + Tribal Knowledge + Compliance Debt problem.*

## 💡 The Solution: Agentic Orchestration
LegacyGuard AI is a multi-agent system that acts as a "Digital Archaeologist + Safe Executor" for legacy environments. Instead of feeding a raw database dump to a single LLM prompt, we built a tiered orchestration pipeline using **Google Gemini** and **Streamlit**.

### The Agent Roster:
1. **Scout Agent:** Ingests raw, undocumented fixed-width strings (e.g., COBOL) and dynamically maps the schema.
2. **Knowledge Bridge Agent:** Applies "tribal knowledge" to translate raw mappings into actionable, plain-English profiles.
3. **Compliance Agent:** Acts as the strict guardrail, evaluating the modernized profile against rigid regulatory frameworks (e.g., RBI Guidelines) to approve or halt workflows.
4. **Execution Orchestrator (Boss Agent):** Coordinates the flow, handles API failovers gracefully, and logs every step into an immutable Audit Trail.

## ⚙️ Architecture Flow
*(Insert the Mermaid Diagram code here or upload an image of the diagram we generated earlier)*

## 🚀 How to Run the Prototype Locally
Because this system requires direct access to enterprise VPCs and sensitive data, the MVP is designed to be run locally, simulating an internal enterprise deployment.

**1. Clone the repository:**
\`\`\`bash
git clone https://github.com/YOUR_USERNAME/legacyguard-ai.git
cd legacyguard-ai
\`\`\`

**2. Install dependencies:**
\`\`\`bash
pip install -r requirements.txt
\`\`\`

**3. Set your Gemini API Key:**
* Windows (PowerShell): `$env:GEMINI_API_KEY="your_api_key_here"`
* Mac/Linux: `export GEMINI_API_KEY="your_api_key_here"`

**4. Boot the Orchestrator:**
\`\`\`bash
streamlit run ui/app.py
\`\`\`
*Navigate to `http://localhost:8501`. Enter mock ID `10045892` for a clean approval, or `10045893` to see the Compliance Agent successfully block a high-risk transaction.*

## ⚠️ Honest Risk Analysis (The "No-Loophole" Defense)
* **Technical Risk:** Hallucinations during schema mapping. *Mitigation:* The Verifier framework ensures deterministic checks against raw strings. Temperature is locked at `0.0`.
* **Business Risk:** Enterprises will not let external Cloud AI touch on-premise mainframes. *Mitigation:* Designed for VPC deployment utilizing Vertex AI's enterprise privacy guarantees.
