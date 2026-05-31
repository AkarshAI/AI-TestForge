import re
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
