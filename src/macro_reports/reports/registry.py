from __future__ import annotations

from macro_reports.reports.average_gdp import AverageGDPReport
from macro_reports.reports.base import BaseReport

""" Здесь можно расширять разнообразие отчётов (упрощённая фабрика) """


class UnknownReportError(ValueError):
    """Отчёт которого нет"""


_REPORTS: dict[str, type[BaseReport]] = {
    # хотим создать новый объект каждый раз
    # и диспетчеризация
    "average-gdp": AverageGDPReport,
}


def get_report(name: str) -> BaseReport:
    """Возвращает объект отчёта по имени из аргумента --report"""
    try:
        report_cls = _REPORTS[name]
    except KeyError as e:
        available = ", ".join(sorted(_REPORTS))
        raise UnknownReportError(
            f"Неизвестный отчёт: {name}. Доступные отчёты: {available}"
        ) from e

    return report_cls()
