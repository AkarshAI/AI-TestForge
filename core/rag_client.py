from typing import Dict

from utilities.logger import logger


class RAGClient:
    """Lightweight RAG client simulation for retrieval and grounding tests."""

    def __init__(self):
        self._documents = {
            "Capital of India": {
                "context": "New Delhi is the capital of India and the seat of government.",
                "answer": "The capital of India is New Delhi",
                "source": "world_facts.txt",
            },
            "Capital of France": {
                "context": "Paris is the capital city of France and a major European destination.",
                "answer": "The capital of France is Paris",
                "source": "world_facts.txt",
            },
            "Capital of Japan": {
                "context": "Tokyo is the capital of Japan and known for its modern skyline.",
                "answer": "The capital of Japan is Tokyo",
                "source": "world_facts.txt",
            },
        }

    def ask(self, question: str) -> Dict[str, str]:
        query = question.strip()
        result = self._documents.get(
            query,
            {
                "context": "",
                "answer": "No relevant passage found.",
                "source": "unknown",
            },
        )
        logger.debug("RAG query executed", extra={"question": question, "source": result["source"]})
        return {
            "context": result["context"],
            "answer": result["answer"],
            "source": result["source"],
        }
