import pytest

from evaluators.groundedness import evaluate_groundedness
from utilities.file_loader import load_json


test_data = load_json("testdata/prompts.json")


@pytest.mark.llm
@pytest.mark.regression
@pytest.mark.parametrize("data", test_data)
def test_groundedness(llm_client, data):
    result = llm_client.ask(data["question"])
    assert evaluate_groundedness(result["answer"], data["expected"])
