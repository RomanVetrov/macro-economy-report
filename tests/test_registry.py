import pytest

from macro_reports.reports.average_gdp import AverageGDPReport
from macro_reports.reports.registry import UnknownReportError, get_report


def test_get_report_returns_average_gdp() -> None:
    """по имени "average-gdp" возвращается объект нужного класса"""
    report = get_report("average-gdp")
    assert isinstance(report, AverageGDPReport)


def test_get_report_raises_on_unknown_name() -> None:
    """по неизвестному имени кидается кастом понятная ошибка UnknownReportError"""
    with pytest.raises(UnknownReportError) as exc:
        get_report("no-such-report")

    assert "Неизвестный отчёт" in str(exc.value)
    assert "average-gdp" in str(exc.value)
