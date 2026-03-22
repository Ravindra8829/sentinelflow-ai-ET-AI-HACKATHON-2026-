from pydantic import BaseModel, Field

class PaymentRequest(BaseModel):
    amount: int = Field(gt=0, lt=100000)

def validate_payment(data):
    try:
        PaymentRequest(**data)
        return True
    except Exception as e:
        return False
