import pytest

from evaluators.reasoning import (
    evaluate_reasoning
)


@pytest.mark.agent
@pytest.mark.regression
def test_reasoning(
        agent_client
):

    result = agent_client.run(
        "Weather in Mumbai"
    )

    assert evaluate_reasoning(
        result["reasoning"]
    )