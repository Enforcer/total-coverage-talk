from typing import Iterator

import httpx
from fastapi import Depends, FastAPI, Request, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from subscriptions import anonymization
from subscriptions.db import Base, session_factory
from subscriptions.models import PaymentCardDetails
from subscriptions.payments_gateway import PaymentCardDto, PaymentsGateway

app = FastAPI()


def user_id(request: Request) -> int:
    return int(request.headers["X-Auth-Id"])


def session() -> Iterator[Session]:
    _session = session_factory()
    yield _session
    _session.close()


@app.on_event("startup")
def setup() -> None:
    Base.metadata.create_all(bind=session_factory.kw["bind"])


class PaymentCardPayload(BaseModel):
    card_number: str
    names: str
    cvc: str


@app.post("/payment-cards")
def store_payment_card(
    payload: PaymentCardPayload,
    user_id: int = Depends(user_id),
    session: Session = Depends(session),
) -> Response:
    payment_card = PaymentCardDetails(
        owner_id=user_id,
        card_number=anonymization.anonymize_card_number(payload.card_number),
        names=payload.names,
        cvc=anonymization.anonymize_cvc(payload.cvc),
    )
    session.add(payment_card)
    session.commit()
    return Response(status_code=201)


@app.post("/payment-cards-in-external-system")
def store_payment_card_in_external_system(
    payload: PaymentCardPayload,
    user_id: int = Depends(user_id),
    payments_gateway: PaymentsGateway = Depends(),
) -> Response:
    dto = PaymentCardDto(
        user_id=user_id,
        card_number=payload.card_number,
        names=payload.names,
        cvc=payload.cvc,
    )
    payments_gateway.store_payment_card(dto)
    return Response(status_code=201)


@app.get("/payment-cards")
def retrieve_payment_card(
    user_id: int = Depends(user_id),
    session: Session = Depends(session),
) -> JSONResponse:
    cards = session.query(PaymentCardDetails).filter_by(owner_id=user_id).all()

    return JSONResponse(
        [
            {
                "card_number": card.card_number,
                "names": card.names,
                "cvc": card.cvc,
            }
            for card in cards
        ]
    )
