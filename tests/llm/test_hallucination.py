import pytest

from evaluators.hallucination \
import evaluate_hallucination

from utilities.file_loader \
import load_json

test_data = load_json(
    "testdata/prompts.json"
)
@pytest.mark.llm

@pytest.mark.hallucination

@pytest.mark.regression

@pytest.mark.parametrize(
    "data",
    test_data
)
def test_hallucination(
        llm_client,
        data
):

    result = llm_client.ask(
        data["question"]
    )

    hallucinated = \
        evaluate_hallucination(
            result["answer"],
            data["expected"]
        )

    assert hallucinated is False