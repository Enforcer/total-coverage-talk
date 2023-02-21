
def is_error() -> bool:
    return False


def foo() -> str:
    value = "OK" if not is_error() else "ERROR"
    return value
