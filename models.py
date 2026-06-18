from sqlalchemy import Column, Float, Integer, String

from database import Base


class CreditCard(Base):
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True, index=True)
    card_name = Column(String, nullable=False)
    issuer = Column(String, nullable=False)
    category = Column(String, nullable=False, index=True)
    reward_rate = Column(Float, nullable=False)
    max_cashback = Column(Float, nullable=False)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    merchant = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    recommended_card = Column(String, nullable=False)
    cashback = Column(Float, nullable=False)
