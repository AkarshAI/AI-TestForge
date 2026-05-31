import csv
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
