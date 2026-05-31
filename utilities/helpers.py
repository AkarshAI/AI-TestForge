from typing import Any


def normalize_text(value: str) -> str:
    """Normalize text for consistent comparisons."""
    return " ".join(value.lower().strip().split())


def ensure_not_empty(value: Any, label: str) -> None:
    """Raise a ValueError when a required value is empty."""
    if value is None or (isinstance(value, str) and not value.strip()):
        raise ValueError(f"{label} must not be empty")
