from typing import Dict

from utilities.logger import logger


class AgentClient:
    """Agent simulator for tool selection and reasoning flows."""

    def __init__(self):
        self._tool_map = {
            "weather": {
                "tool": "weather_tool",
                "answer": "Mumbai temperature is 30C",
                "reasoning": "The query requests weather information, so the weather tool is required.",
            },
            "search": {
                "tool": "web_search",
                "answer": "Latest AI news: new model improves retrieval accuracy.",
                "reasoning": "The query asks for general information, so the web search tool provides an answer.",
            },
        }

    def run(self, query: str) -> Dict[str, str]:
        text = query.strip().lower()
        if "weather" in text:
            tool = self._tool_map["weather"]
        elif "search" in text or "find" in text:
            tool = self._tool_map["search"]
        else:
            tool = {
                "tool": "fallback_tool",
                "answer": "I am not able to route that request to a specialized tool.",
                "reasoning": "The intent is not recognized by available tool handlers.",
            }
        logger.debug("Agent executed", extra={"query": query, "tool": tool["tool"]})
        return {
            "query": query,
            "tool_used": tool["tool"],
            "reasoning": tool["reasoning"],
            "answer": tool["answer"],
        }
