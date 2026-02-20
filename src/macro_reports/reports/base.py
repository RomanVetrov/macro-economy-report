from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterable, Mapping


class BaseReport(ABC):
    """базовый класс для всех отчётов"""

    @abstractmethod
    def build(self, rows: Iterable[Mapping[str, Any]]) -> Any:
        """должен вернуть результат отчёта на основе переданных данных"""
        raise NotImplementedError
