def evaluate_latency(response_time: float, threshold: float = 2.0) -> bool:
    """Validate that the response time is within acceptable limits."""
    return response_time <= threshold
