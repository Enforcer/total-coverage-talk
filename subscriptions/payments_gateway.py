import httpx
from attrs import define


@define(frozen=True)
class PaymentCardDto:
    user_id: int
    card_number: str
    names: str
    cvc: str


class PaymentsGateway:
    def store_payment_card(self, dto: PaymentCardDto) -> None:
        httpx.post(
            "https://example.tech/payment-cards",
            json={
                "card_number": dto.card_number,
                "names": dto.names,
                "cvc": dto.cvc,
                "user_id": dto.user_id,
            },
        )
