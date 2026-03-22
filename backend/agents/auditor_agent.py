from pydantic import BaseModel, Field

class Validation(BaseModel):
    value: int = Field(gt=0)

def audit_step(step):

    print(f"Auditing step: {step}")

    return {"status": "approved"}
