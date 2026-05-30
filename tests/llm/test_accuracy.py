import pytest

from evaluators.factuality \
import evaluate_factuality

from utilities.file_loader \
import load_json



test_data = load_json(
    "testdata/prompts.json"
)

@pytest.mark.llm

@pytest.mark.smoke

@pytest.mark.parametrize(
    "data",
    test_data
)
def test_factual_accuracy(
        llm_client,
        data
):

    result = llm_client.ask(
        data["question"]
    )

    is_correct = \
        evaluate_factuality(
            result["answer"],
            data["expected"]
        )

    assert is_correct