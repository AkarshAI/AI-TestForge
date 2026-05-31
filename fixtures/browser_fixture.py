import pytest

from core.browser_client import BrowserClient


@pytest.fixture(scope="session")
def browser_client() -> BrowserClient:
    return BrowserClient()
