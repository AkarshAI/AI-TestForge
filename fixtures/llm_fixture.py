import pytest

from core.llm_client import LLMClient


@pytest.fixture(scope="session")
def llm_client() -> LLMClient:
    return LLMClient()
