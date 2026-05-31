import time
from typing import Dict

from utilities.logger import logger


class LLMClient:
    """Simulated LLM client for evaluation and regression testing."""

    def __init__(self, model_name: str = "ai-test-llm"):
        self.model_name = model_name
        self._knowledge = {
            "Capital of India": "The capital of India is New Delhi",
            "Capital of France": "Paris",
            "Capital of Japan": "Tokyo",
            "What is the weather in Mumbai?": "Mumbai is warm and humid today",
            "Who wrote Hamlet?": "Hamlet was written by William Shakespeare",
        }

    def ask(self, question: str) -> Dict[str, object]:
        start_time = time.perf_counter()
        answer = self._knowledge.get(question.strip(), "I am not sure about that.")
        latency = time.perf_counter() - start_time
        logger.debug(
            "LLM request completed",
            extra={"question": question, "model": self.model_name, "latency": latency},
        )
        return {
            "question": question,
            "answer": answer,
            "latency": latency,
            "model": self.model_name,
        }
