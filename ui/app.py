import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from orchestrator.nasiko_flow import run_legacy_extraction_flow

# ... the rest of your app.py code remains exactly the same ...
from orchestrator.nasiko_flow import run_legacy_extraction_flow

st.set_page_config(page_title="LegacyGuard AI", layout="wide")

st.title("🛡️ LegacyGuard AI Orchestrator")
st.caption("Bridging 1995 Mainframes with Agentic AI")

st.markdown("### KYC / Loan Eligibility Workflow")
cust_id = st.text_input("Enter Customer ID to extract from Legacy Core (Try: 10045892)")

if st.button("Execute Agentic Workflow"):
    with st.spinner("Waking up Execution Orchestrator..."):
        result = run_legacy_extraction_flow(cust_id)
        
        col1, col2 = st.columns(2)
        with col1:
            st.success("Modernized Profile Insight")
            st.write(result["modern_insight"])
            
            st.warning("Compliance & Guardrails")
            st.write(result["compliance_status"])
            
        with col2:
            st.info("System Audit Trail (Boss Agent Logs)")
            for log in result["audit_trail"]:
                st.code(log)