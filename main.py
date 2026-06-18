from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

import crud
from database import Base, SessionLocal, engine, get_db
from schemas import (
    CreditCardCreate,
    CreditCardResponse,
    CreditCardUpdate,
    RecommendRequest,
    RecommendResponse,
    TransactionResponse,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        crud.seed_cards(db)
    finally:
        db.close()
    yield


app = FastAPI(
    title="Credit Card Rewards Optimizer API",
    description="Recommends the best credit card and estimates cashback for transactions.",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {
        "message": "Credit Card Rewards Optimizer API",
        "docs": "/docs",
        "endpoints": {
            "cards": "/cards",
            "recommend": "/recommend",
            "transactions": "/transactions",
        },
    }


@app.post("/cards", response_model=CreditCardResponse, status_code=201)
def create_card(card: CreditCardCreate, db: Session = Depends(get_db)):
    return crud.create_card(db, card)


@app.get("/cards", response_model=list[CreditCardResponse])
def list_cards(db: Session = Depends(get_db)):
    return crud.get_cards(db)


@app.put("/cards/{card_id}", response_model=CreditCardResponse)
def update_card(
    card_id: int, card: CreditCardUpdate, db: Session = Depends(get_db)
):
    return crud.update_card(db, card_id, card)


@app.delete("/cards/{card_id}", status_code=204)
def delete_card(card_id: int, db: Session = Depends(get_db)):
    crud.delete_card(db, card_id)


@app.post("/recommend", response_model=RecommendResponse)
def recommend(request: RecommendRequest, db: Session = Depends(get_db)):
    card, cashback = crud.recommend_card(
        db, request.merchant, request.category, request.amount
    )
    return RecommendResponse(
        recommended_card=card.card_name,
        reward_rate=card.reward_rate,
        estimated_cashback=cashback,
    )


@app.get("/transactions", response_model=list[TransactionResponse])
def list_transactions(db: Session = Depends(get_db)):
    return crud.get_transactions(db)
