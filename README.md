# 🛡️ LegacyGuard AI Orchestrator

**Bridging 1995 Mainframes with Agentic AI**
*Built for Google Fragfest Hackathon - Track B*

## 🚨 The Core Problem
**Decades of accumulated process debt in the enterprise sector.**
Most AI pilots fail (95%) not due to model capability, but the inability to safely integrate with ancient mainframes, siloed databases, compliance layers, and the tribal knowledge held by retiring experts. 
* India’s $300B+ IT services industry is at risk of losing its global edge unless it masters legacy integration in the agentic AI era.
* We don’t have an AI problem. We have a *Legacy + Tribal Knowledge + Compliance Debt problem.*

## 💡 The Solution: Agentic Orchestration
LegacyGuard AI is a multi-agent system that acts as a "Digital Archaeologist + Safe Executor" for legacy environments. Instead of feeding a raw database dump to a single hallucination-prone LLM prompt, we built a tiered, deterministic orchestration pipeline.

### The Agent Roster:
1. **Scout Agent (gemini-3.1-flash-lite):** Ingests raw, undocumented fixed-width strings (e.g., COBOL/EBCDIC) and dynamically maps the positional schema.
2. **Knowledge Bridge Agent (gemini-3.1-flash-lite):** Applies human "tribal knowledge" to translate raw mappings and codes into actionable, plain-English profiles.
3. **Compliance Agent (gemini-3.5-flash):** Acts as the strict guardrail, evaluating the modernized profile against rigid regulatory frameworks (e.g., RBI Guidelines) to approve or halt workflows.
4. **Execution Orchestrator (Boss Agent):** Coordinates the Python flow, handles API failovers (503 traffic spikes) gracefully, and logs every step into an immutable Audit Trail.

## ⚙️ Architecture Flow


## 🗄️ The Mock Legacy Infrastructure
To prove our orchestration works, we simulate a legacy banking core using a mock VSAM hierarchical file structure. When queried, it does not return clean JSON; it returns an undocumented, 46-character fixed-width flat file (COBOL Copybook format). 

**Available Test Cases:**
* `10045892`: Clean / Medium Risk (Demonstrates auto-approval)
* `10045893`: Closed / High Risk (Demonstrates Compliance Agent halting the transaction)
* `99999999`: Custom Test (Demonstrates dynamic lookup)

---

## 🚀 How to Run the Prototype

### Option A: Local Development (Hot-Reloading for Live Demos)
Because this system requires direct access to enterprise VPCs and sensitive data, the MVP is designed to be run locally, simulating an internal enterprise deployment.

**1. Clone the repository:**
```bash
git clone (https://github.com/JensonCode007/Multi-Agent-Orchestrator.git/)
```
