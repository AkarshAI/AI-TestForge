def evaluate_groundedness(answer: str, context: str) -> bool:
    """Validate whether the answer is grounded in the provided retrieval context."""
    answer_words = {token for token in answer.lower().split() if token.isalpha()}
    context_words = {token for token in context.lower().split() if token.isalpha()}
    overlap = answer_words.intersection(context_words)
    return len(overlap) >= 1
