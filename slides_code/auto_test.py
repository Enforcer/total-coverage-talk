import pytest


class Phones:
    def register(self, name: str, number: str) -> None:
        pass


@pytest.fixture()
def phones() -> Phones:
    return Phones()


def test_dialing_another_phone_makes_it_ring() -> None:
    phones.register("Alice", "111")
    phones.register("Bob", "222")

    phones.of("Alice").dial("Bob")

    assert phones.of("Bob").is_ringing()
