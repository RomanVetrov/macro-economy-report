from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Any, Iterable, Mapping

from macro_reports.reports.base import BaseReport


@dataclass(frozen=True)
class CountryAverageGDP:  # удобство, из коробки. Описывает строчку отчёта (страна, среднее)
    country: str
    average_gdp: float


class AverageGDPReport(BaseReport):
    """Отчёт со средним ВВП по странам."""

    def build(self, rows: Iterable[Mapping[str, Any]]) -> list[CountryAverageGDP]:
        """Считает сумму, затем средний ВВП по каждой стране и возвращает отсортированный список
        датаклассов
        """
        sums: dict[str, float] = defaultdict(float)  # {страна: сумма всех её gdp}
        counts: dict[str, int] = defaultdict(int)  # {страна: сколько раз была}

        for row in rows:
            country = str(row["country"])
            gdp = float(row["gdp"])
            sums[country] += gdp
            counts[country] += 1

        result: list[CountryAverageGDP] = [
            CountryAverageGDP(
                country=country, average_gdp=sums[country] / counts[country]
            )
            for country in sums
        ]

        # сортируем по среднему ввп по убыванию.
        # если среднее одинаковое - сортируем по названию страны, чтобы результат был стабильный
        result.sort(key=lambda row: (-row.average_gdp, row.country))
        return result
