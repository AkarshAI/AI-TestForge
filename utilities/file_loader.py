import csv
import json
from pathlib import Path
from typing import List, Dict


def resolve_path(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()


def load_json(path: str | Path) -> List[Dict[str, str]]:
    resolved_path = resolve_path(path)
    with open(resolved_path, encoding='utf-8') as handle:
        return json.load(handle)


def load_csv(path: str | Path) -> List[Dict[str, str]]:
    resolved_path = resolve_path(path)
    with open(resolved_path, encoding='utf-8', newline='') as handle:
        reader = csv.DictReader(handle)
        return [row for row in reader]
