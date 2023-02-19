def anonymize_cvc(cvc: str) -> str:
    return "*" * len(cvc)


def anonymize_card_number(card_number: str) -> str:
    return f"{card_number[:4]} **** **** {card_number[-4:]}"
