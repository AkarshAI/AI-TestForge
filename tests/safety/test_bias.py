import pytest

from evaluators.bias import evaluate_bias
from utilities.file_loader import load_json


test_data = load_json("testdata/safety_prompts.json")


@pytest.mark.safety
@pytest.mark.regression
@pytest.mark.parametrize("item", test_data)
def test_bias(item):
    is_unbiased = evaluate_bias(item["prompt"])
    assert is_unbiased == item["expected_bias"]
