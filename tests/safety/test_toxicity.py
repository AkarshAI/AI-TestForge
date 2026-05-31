import pytest

from evaluators.toxicity import evaluate_toxicity
from utilities.file_loader import load_json


test_data = load_json("testdata/safety_prompts.json")


@pytest.mark.safety
@pytest.mark.regression
@pytest.mark.parametrize("item", test_data)
def test_toxicity(item):
    is_toxic = evaluate_toxicity(item["prompt"])
    assert is_toxic == item["expected_toxic"]
