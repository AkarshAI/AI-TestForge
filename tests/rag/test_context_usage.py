import pytest

from evaluators.groundedness import (
    evaluate_groundedness
)


@pytest.mark.rag
@pytest.mark.regression
def test_context_usage(rag_client):

    result = rag_client.ask(
        "Capital of India"
    )

    assert evaluate_groundedness(
        result["answer"],
        result["context"]
    )