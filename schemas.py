from pydantic import BaseModel, Field


class CreditCardCreate(BaseModel):
    card_name: str
    issuer: str
    category: str
    reward_rate: float = Field(ge=0)
    max_cashback: float = Field(ge=0)


class CreditCardUpdate(BaseModel):
    card_name: str
    issuer: str
    category: str
    reward_rate: float = Field(ge=0)
    max_cashback: float = Field(ge=0)


class CreditCardResponse(BaseModel):
    id: int
    card_name: str
    issuer: str
    category: str
    reward_rate: float
    max_cashback: float

    model_config = {"from_attributes": True}


class RecommendRequest(BaseModel):
    merchant: str
    category: str
    amount: float = Field(gt=0)


class RecommendResponse(BaseModel):
    recommended_card: str
    reward_rate: float
    estimated_cashback: float


class TransactionResponse(BaseModel):
    merchant: str
    amount: float
    recommended_card: str
    cashback: float

    model_config = {"from_attributes": True}
