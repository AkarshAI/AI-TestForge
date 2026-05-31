import pytest

from evaluators.retrieval import (
    evaluate_retrieval
)


@pytest.mark.rag
@pytest.mark.smoke
def test_retrieval(rag_client):

    result = rag_client.ask(
        "Capital of India"
    )

    assert evaluate_retrieval(
        result["context"],
        "New Delhi"
    )