import pytest

from evaluators.latency \
import evaluate_latency

from utilities.file_loader \
import load_json

test_data = load_json(
    "testdata/prompts.json"
)


@pytest.mark.parametrize(
    "data",
    test_data
)
def test_latency(
        llm_client,
        data
):

    result = llm_client.ask(
        data["question"]
    )

    assert evaluate_latency(
        result["latency"]
    )