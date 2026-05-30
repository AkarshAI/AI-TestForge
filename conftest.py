import pytest

from core.llm_client import LLMClient


@pytest.fixture
def llm_client():

    return LLMClient()