import pytest

from core.api_client import APIClient


@pytest.fixture(scope="session")
def api_client(request) -> APIClient:
    env = request.config.getoption("--target-env")
    return APIClient(env)
