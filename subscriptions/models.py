from sqlalchemy import Column, Integer, String

from subscriptions.db import Base


class PaymentCardDetails(Base):
    __tablename__ = "payment_card_details"

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, nullable=False)
    card_number = Column(String, nullable=False)
    names = Column(String, nullable=False)
    cvc = Column(String, nullable=False)
