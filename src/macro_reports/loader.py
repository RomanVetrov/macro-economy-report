from __future__ import annotations

import csv
from pathlib import Path
from typing import Iterable


def load_rows(files: Iterable[str]) -> list[dict[str, str]]:
    """Читает переданные CSV-файлы и возвращает список строк в виде словарей"""
    rows: list[dict[str, str]] = []

    for file_path in files:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        with path.open(newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row)

    return rows
