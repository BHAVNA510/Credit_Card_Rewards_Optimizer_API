from __future__ import annotations

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import CreditCard, Transaction
from schemas import CreditCardCreate, CreditCardUpdate


SEED_CARDS = [
    {
        "card_name": "HDFC Millennia",
        "issuer": "HDFC",
        "category": "Shopping",
        "reward_rate": 5.0,
        "max_cashback": 1000.0,
    },
    {
        "card_name": "SBI Cashback",
        "issuer": "SBI",
        "category": "Shopping",
        "reward_rate": 3.0,
        "max_cashback": 500.0,
    },
    {
        "card_name": "ICICI Amazon Pay",
        "issuer": "ICICI",
        "category": "Shopping",
        "reward_rate": 2.0,
        "max_cashback": 300.0,
    },
    {
        "card_name": "Axis Flipkart",
        "issuer": "Axis",
        "category": "Shopping",
        "reward_rate": 4.0,
        "max_cashback": 800.0,
    },
    {
        "card_name": "HDFC Regalia",
        "issuer": "HDFC",
        "category": "Dining",
        "reward_rate": 4.0,
        "max_cashback": 600.0,
    },
    {
        "card_name": "Amex Gold",
        "issuer": "Amex",
        "category": "Dining",
        "reward_rate": 6.0,
        "max_cashback": 1200.0,
    },
]


def seed_cards(db: Session) -> None:
    if db.query(CreditCard).count() > 0:
        return
    for card_data in SEED_CARDS:
        db.add(CreditCard(**card_data))
    db.commit()


def get_cards(db: Session) -> list[CreditCard]:
    return db.query(CreditCard).order_by(CreditCard.id).all()


def get_card(db: Session, card_id: int) -> CreditCard | None:
    return db.query(CreditCard).filter(CreditCard.id == card_id).first()


def create_card(db: Session, card: CreditCardCreate) -> CreditCard:
    db_card = CreditCard(**card.model_dump())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card


def update_card(db: Session, card_id: int, card: CreditCardUpdate) -> CreditCard:
    db_card = get_card(db, card_id)
    if not db_card:
        raise HTTPException(status_code=404, detail="Credit card not found")
    for field, value in card.model_dump().items():
        setattr(db_card, field, value)
    db.commit()
    db.refresh(db_card)
    return db_card


def delete_card(db: Session, card_id: int) -> None:
    db_card = get_card(db, card_id)
    if not db_card:
        raise HTTPException(status_code=404, detail="Credit card not found")
    db.delete(db_card)
    db.commit()


def get_transactions(db: Session) -> list[Transaction]:
    return db.query(Transaction).order_by(Transaction.id).all()


def recommend_card(
    db: Session, merchant: str, category: str, amount: float
) -> tuple[CreditCard, float]:
    matching_cards = (
        db.query(CreditCard)
        .filter(CreditCard.category.ilike(category))
        .order_by(CreditCard.reward_rate.desc(), CreditCard.id.asc())
        .all()
    )
    if not matching_cards:
        raise HTTPException(
            status_code=404,
            detail=f"No credit cards found for category '{category}'",
        )

    best_card = matching_cards[0]
    calculated_cashback = amount * best_card.reward_rate / 100
    cashback = min(calculated_cashback, best_card.max_cashback)

    transaction = Transaction(
        merchant=merchant,
        amount=amount,
        category=category,
        recommended_card=best_card.card_name,
        cashback=cashback,
    )
    db.add(transaction)
    db.commit()

    return best_card, cashback
