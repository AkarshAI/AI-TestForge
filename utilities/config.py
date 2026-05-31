CONFIG = {
    "qa": {
        "base_url": "https://qa.example.com",
    },
    "prod": {
        "base_url": "https://prod.example.com",
    },
}


def get_config(environment: str = "qa") -> dict:
    return CONFIG.get(environment.lower(), CONFIG["qa"])
