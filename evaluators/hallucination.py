def evaluate_hallucination(response: str, expected: str) -> bool:
    """Detect hallucination when the response does not contain the expected fact."""
    if not response:
        return True
    return expected.lower() not in response.lower()
