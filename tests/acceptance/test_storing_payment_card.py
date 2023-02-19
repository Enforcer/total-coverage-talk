from fastapi.testclient import TestClient


def test_customer_can_read_stored_payment_card_details(
    authorized_client: TestClient,
) -> None:
    add_response = authorized_client.post(
        "/payment-cards",
        json={
            "card_number": "4111 1111 1111 1111",
            "names": "John Doe",
            "cvc": "123",
        },
    )
    assert add_response.status_code == 201

    get_response = authorized_client.get("/payment-cards")
    assert get_response.status_code == 200
    assert get_response.json() == [
        {
            "card_number": "4111 **** **** 1111",
            "names": "John Doe",
            "cvc": "***",
        }
    ]


def test_initially_customer_has_no_saved_payments_cards() -> None:
    pass


def test_customer_can_read_only_payment_cards_they_created() -> None:
    pass
