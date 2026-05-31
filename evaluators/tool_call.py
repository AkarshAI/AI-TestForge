def evaluate_tool_call(actual_tool: str, expected_tool: str) -> bool:
    """Validate the tool selection produced by the agent."""
    return actual_tool == expected_tool
