from fastapi import FastAPI

app = FastAPI(title="Mock Core Banking System (1995)")

@app.get("/api/v1/customer/{cust_id}")
def get_legacy_record(cust_id: str):
    # Simulates a messy COBOL fixed-width data dump
    # Format: ID(8)|NAME(15)|DOB(8)|BAL(10)|STAT(1)|RISK_C(2)
    mock_db = {
        "10045892": "10045892KUMAR,R        198504120004589200A R4",
        "10045893": "10045893SHARMA,P       199011050000005000C R9"
    }
    return {"raw_data": mock_db.get(cust_id, "ERR: CUST NOT FOUND")}