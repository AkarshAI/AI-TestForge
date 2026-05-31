def evaluate_reasoning(reasoning: str) -> bool:
    """Verify the agent reasoning string is meaningful and not empty."""
    return bool(reasoning and reasoning.strip())
