def evaluate_retrieval(context: str, expected: str) -> bool:
    """Ensure the retrieval context contains the expected passage or entity."""
    return expected.lower() in context.lower()
