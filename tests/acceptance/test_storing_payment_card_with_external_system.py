from typing import Any

from fastapi.testclient import TestClient
from mockito import verify

from subscriptions.payments_gateway import PaymentCardDto, PaymentsGateway


def test_payment_card_is_stored_in_external_system(
    authorized_client: TestClient,
    user_id: int,
    when: Any,
) -> None:
    when(PaymentsGateway).store_payment_card(...).thenReturn(None)

    add_response = authorized_client.post(
        "/payment-cards-in-external-system",
        json={
            "card_number": "4000-0000-0000-0002",
            "names": "Janine Doe",
            "cvc": "321",
        },
    )
    assert add_response.status_code == 201

    verify(PaymentsGateway, times=1).store_payment_card(
        PaymentCardDto(
            user_id=user_id,
            card_number="4000-0000-0000-0002",
            names="Janine Doe",
            cvc="321",
        )
    )
