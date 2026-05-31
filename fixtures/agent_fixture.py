import pytest

from core.agent_client import AgentClient


@pytest.fixture(scope="session")
def agent_client() -> AgentClient:
    return AgentClient()
