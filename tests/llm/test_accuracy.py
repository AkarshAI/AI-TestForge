import pytest

from utilities.file_loader import (
    load_json
)

test_data = load_json(
    "testdata/prompts.json"
)

@pytest.mark.parametrize(
    "data",
    test_data,
    ids=[
        item["question"]
        for item in test_data
    ]
)
def test_capital_answers(llm_client, data):
    assert llm_client.ask(data["question"]) == data["expected"]
