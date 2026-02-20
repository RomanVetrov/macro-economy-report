from macro_reports.render import render_table
from macro_reports.reports.average_gdp import CountryAverageGDP


def test_render_table_for_dataclass_rows() -> None:
    """Проверяет визуализацию списка датаклассов в таблицу.
    Убеждаемся, что названия полей датакласса становятся заголовками,
    а значения атрибутов попадают в соответствующие строки таблицы.
    """
    rows = [
        CountryAverageGDP(country="USA", average_gdp=20.0),
        CountryAverageGDP(country="China", average_gdp=10.0),
    ]

    table = render_table(rows)

    assert "country" in table
    assert "average_gdp" in table
    assert "USA" in table
    assert "China" in table


def test_render_table_empty() -> None:
    """отсутствие данных"""
    assert render_table([]) == "Нет данных"
