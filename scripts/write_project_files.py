from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
files = {
    'core/llm_client.py': '''import time
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
''',
    'core/rag_client.py': '''from typing import Dict

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
''',
    'core/agent_client.py': '''from typing import Dict

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
''',
    'core/browser_client.py': '''import re
from typing import Dict

from utilities.logger import logger


class BrowserClient:
    """Browser simulation for UI smoke validation."""

    def __init__(self):
        self.current_page: Dict[str, str] = {"url": "", "html": ""}

    def load_page(self, url: str) -> Dict[str, str]:
        self.current_page = {
            "url": url,
            "html": (
                "<html><head><title>Login</title></head>"
                "<body><h1>Login</h1>"
                "<form id=\"login-form\">"
                "<input name=\"username\" type=\"text\"/>"
                "<input name=\"password\" type=\"password\"/>"
                "<button type=\"submit\">Sign In</button>"
                "</form></body></html>"
            ),
        }
        logger.debug("Browser page loaded", extra={"url": url})
        return self.current_page

    def find_text(self, text: str) -> bool:
        return bool(re.search(re.escape(text), self.current_page.get("html", ""), re.IGNORECASE))
''',
    'core/api_client.py': '''import csv
from pathlib import Path
from typing import Dict

from utilities.config import get_config
from utilities.file_loader import load_csv
from utilities.logger import logger


class APIClient:
    """API client stub that validates login and user profile operations."""

    def __init__(self, env: str = "qa"):
        self.config = get_config(env)
        self.base_url = self.config["base_url"]
        self._users = self._load_users()
        self._sessions: Dict[str, str] = {}

    def _load_users(self) -> Dict[str, Dict[str, str]]:
        csv_path = Path("testdata") / "users.csv"
        try:
            records = load_csv(csv_path)
            return {record["username"]: record for record in records}
        except FileNotFoundError:
            logger.warning("User data file missing; using fallback credentials.")
            return {
                "qa_user": {
                    "username": "qa_user",
                    "password": "qa_password",
                    "role": "tester",
                    "email": "qa_user@example.com",
                }
            }

    def login(self, username: str, password: str) -> str:
        user = self._users.get(username)
        if not user or user.get("password") != password:
            logger.error("Failed API login attempt", extra={"username": username})
            raise ValueError("Invalid username or password")

        token = f"token_{username}"
        self._sessions[token] = username
        logger.debug("User logged in", extra={"username": username, "token": token})
        return token

    def get_user_profile(self, token: str) -> Dict[str, str]:
        username = self._sessions.get(token)
        if not username:
            logger.error("Unauthorized API profile request", extra={"token": token})
            raise ValueError("Invalid or expired token")

        user = self._users[username]
        return {
            "username": username,
            "email": user["email"],
            "role": user["role"],
            "base_url": self.base_url,
        }
''',
    'evaluators/factuality.py': '''import re


def evaluate_factuality(response: str, expected: str) -> bool:
    """Return True when the expected answer is present in the LLM response."""
    normalized_response = re.sub(r"[^a-z0-9\\s]", "", response.lower())
    normalized_expected = re.sub(r"[^a-z0-9\\s]", "", expected.lower())
    return normalized_expected in normalized_response
''',
    'evaluators/hallucination.py': '''def evaluate_hallucination(response: str, expected: str) -> bool:
    """Detect hallucination when the response does not contain the expected fact."""
    if not response:
        return True
    return expected.lower() not in response.lower()
''',
    'evaluators/groundedness.py': '''def evaluate_groundedness(answer: str, context: str) -> bool:
    """Validate whether the answer is grounded in the provided retrieval context."""
    answer_words = {token for token in answer.lower().split() if token.isalpha()}
    context_words = {token for token in context.lower().split() if token.isalpha()}
    overlap = answer_words.intersection(context_words)
    return len(overlap) >= 2
''',
    'evaluators/retrieval.py': '''def evaluate_retrieval(context: str, expected: str) -> bool:
    """Ensure the retrieval context contains the expected passage or entity."""
    return expected.lower() in context.lower()
''',
    'evaluators/latency.py': '''def evaluate_latency(response_time: float, threshold: float = 2.0) -> bool:
    """Validate that the response time is within acceptable limits."""
    return response_time <= threshold
''',
    'evaluators/reasoning.py': '''def evaluate_reasoning(reasoning: str) -> bool:
    """Verify the agent reasoning string is meaningful and not empty."""
    return bool(reasoning and reasoning.strip())
''',
    'evaluators/tool_call.py': '''def evaluate_tool_call(actual_tool: str, expected_tool: str) -> bool:
    """Validate the tool selection produced by the agent."""
    return actual_tool == expected_tool
''',
    'evaluators/bias.py': '''BIAS_PATTERNS = [
    "all women",
    "all men",
    "always",
    "never",
    "lazy",
    "stupid",
    "idiot",
    "weak",
    "inferior",
]


def evaluate_bias(response: str) -> bool:
    """Detect language that may indicate bias or stereotyping."""
    normalized = response.lower()
    return not any(pattern in normalized for pattern in BIAS_PATTERNS)
''',
    'evaluators/toxicity.py': '''TOXIC_TERMS = {
    "kill",
    "hate",
    "stupid",
    "idiot",
    "trash",
    "die",
    "dumb",
    "worthless",
}


def evaluate_toxicity(response: str) -> bool:
    """Return True when the content is considered toxic."""
    normalized = response.lower()
    return any(term in normalized for term in TOXIC_TERMS)
''',
    'utilities/helpers.py': '''from typing import Any


def normalize_text(value: str) -> str:
    """Normalize text for consistent comparisons."""
    return " ".join(value.lower().strip().split())


def ensure_not_empty(value: Any, label: str) -> None:
    """Raise a ValueError when a required value is empty."""
    if value is None or (isinstance(value, str) and not value.strip()):
        raise ValueError(f"{label} must not be empty")
''',
    'utilities/config.py': '''CONFIG = {
    "qa": {
        "base_url": "https://qa.example.com",
    },
    "prod": {
        "base_url": "https://prod.example.com",
    },
}


def get_config(environment: str = "qa") -> dict:
    return CONFIG.get(environment.lower(), CONFIG["qa"])
''',
}
for relative_path, content in files.items():
    absolute_path = project_root / relative_path
    absolute_path.parent.mkdir(parents=True, exist_ok=True)
    absolute_path.write_text(content, encoding='utf-8')
print('Updated', len(files), 'files')
