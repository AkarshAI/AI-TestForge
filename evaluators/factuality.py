import re


def evaluate_factuality(response: str, expected: str) -> bool:
    """Return True when the expected answer is present in the LLM response."""
    normalized_response = re.sub(r"[^a-z0-9\s]", "", response.lower())
    normalized_expected = re.sub(r"[^a-z0-9\s]", "", expected.lower())
    return normalized_expected in normalized_response
