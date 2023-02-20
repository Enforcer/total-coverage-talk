import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine

from subscriptions.api import app
from subscriptions.db import session_factory

users_ids = iter(range(1, 1_000_000))


@pytest.fixture(autouse=True, scope="session")
def engine_for_testing(tmp_path_factory: pytest.TempPathFactory) -> None:
    path = tmp_path_factory.mktemp("test_db")
    test_engine = create_engine(f"sqlite:///{path}/subscriptions.db")
    session_factory.configure(bind=test_engine)


@pytest.fixture()
def client() -> TestClient:
    with TestClient(app) as _client:
        yield _client


@pytest.fixture()
def user_id() -> int:
    return next(users_ids)


@pytest.fixture()
def authorized_client(client: TestClient, user_id: int) -> TestClient:
    client.headers["X-Auth-Id"] = str(user_id)
    return client
