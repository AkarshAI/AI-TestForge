import pytest

from evaluators.tool_call import (
    evaluate_tool_call
)


@pytest.mark.agent
@pytest.mark.smoke
def test_tool_call(
        agent_client
):

    result = agent_client.run(
        "Weather in Mumbai"
    )

    assert evaluate_tool_call(
        result["tool_used"],
        "weather_tool"
    )