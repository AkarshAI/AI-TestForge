import pytest

from core.rag_client import RAGClient


@pytest.fixture(scope="session")
def rag_client() -> RAGClient:
    return RAGClient()
