TOXIC_TERMS = {
    "kill",
    "hate",
    "stupid",
    "idiot",
    "trash",
    "die",
    "dumb",
    "worthless",
    "bad",
    "lazy",
}


def evaluate_toxicity(response: str) -> bool:
    """Return True when the content is considered toxic."""
    normalized = response.lower()
    return any(term in normalized for term in TOXIC_TERMS)
