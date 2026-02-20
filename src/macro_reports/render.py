from __future__ import annotations

from dataclasses import is_dataclass
from typing import Any, Iterable

from tabulate import tabulate


def render_table(rows: Iterable[Any]) -> str:
    """Делает текстовую таблицу для вывода в терминал"""
    rows = list(rows)

    if not rows:
        return "Нет данных"

    first = rows[0]

    # если строки - dataclass (как CountryAverageGDP), делаем таблицу по полям dataclass
    if is_dataclass(first):
        headers = list(first.__dataclass_fields__.keys())
        data = [[getattr(r, h) for h in headers] for r in rows]
        return tabulate(data, headers=headers, tablefmt="github")

    # если строки - словари
    if isinstance(first, dict):
        headers = list(first.keys())
        data = [[r.get(h) for h in headers] for r in rows]
        return tabulate(data, headers=headers, tablefmt="github")

    # если пришло что-то неожиданное(или простое) - просто печатаем как есть
    return tabulate([[str(r)] for r in rows], headers=["value"], tablefmt="github")
