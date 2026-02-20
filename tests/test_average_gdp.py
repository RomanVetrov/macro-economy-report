from macro_reports.reports.average_gdp import AverageGDPReport


def test_average_gdp_single_country() -> None:
    """
    Проверяет корректность расчета среднего ВВП.
    Убеждаемся, что сумма значений правильно делится на количество записей
    для одной страны.
    """
    rows = [
        {"country": "A", "gdp": 10},
        {"country": "A", "gdp": 20},
        {"country": "A", "gdp": 30},
    ]

    result = AverageGDPReport().build(rows)

    assert len(result) == 1
    assert result[0].country == "A"
    assert result[0].average_gdp == 20.0


def test_average_gdp_multiple_countries_sorted_desc() -> None:
    """
    Проверяем основную логику сортировки отчёта.
    Результат должен быть отсортирован по значению среднего ВВП
    в порядке убывания (от богатых стран к бедным).
    """
    rows = [
        {"country": "A", "gdp": 10},
        {"country": "A", "gdp": 30},
        {"country": "B", "gdp": 100},
        {"country": "C", "gdp": 25},
        {"country": "C", "gdp": 25},
    ]

    result = AverageGDPReport().build(rows)

    assert [r.country for r in result] == ["B", "C", "A"]
    assert [r.average_gdp for r in result] == [100.0, 25.0, 20.0]


def test_average_gdp_tie_breaker_by_country_name() -> None:
    """
    Проверяет детерминированность сортировки.
    Если средний ВВП у стран совпадает, они должны быть отсортированы
    строго по алфавиту названия страны.
    """
    rows = [
        {"country": "B", "gdp": 10},
        {"country": "A", "gdp": 10},
    ]

    result = AverageGDPReport().build(rows)

    # одинаковое среднее => сортировка по названию страны
    assert [r.country for r in result] == ["A", "B"]
