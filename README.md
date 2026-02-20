# Macro Economy Report

CLI-инструмент для формирования отчётов по макроэкономическим данным из CSV-файлов.

[![Python](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![pytest](https://img.shields.io/badge/pytest-10%20passed-brightgreen?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![coverage](https://img.shields.io/badge/coverage-84%25-brightgreen)](https://github.com/pytest-dev/pytest-cov)
[![tabulate](https://img.shields.io/badge/tabulate-0.9.0-lightgrey)](https://github.com/astanin/python-tabulate)

## Демо

[![asciicast](https://asciinema.org/a/so71h5z1tVHpJbjx.svg)](https://asciinema.org/a/so71h5z1tVHpJbjx)

## Установка

```bash
git clone <repo-url>
cd macro_economy_report
uv sync
```

## Запуск

```bash
uv run macro-reports --files examples/economic1.csv examples/economic2.csv --report average-gdp
```

Или через модуль напрямую:

```bash
uv run python -m macro_reports --files examples/economic1.csv --report average-gdp
```

Пример вывода:

```
| country        |   average_gdp |
|----------------|---------------|
| United States  |       23923.7 |
| China          |       17810.3 |
| Japan          |        4467   |
| Germany        |        4138.3 |
| ...            |           ... |
```

## Как добавить новый отчёт

1. Создать файл в `src/macro_reports/reports/`, унаследовав `BaseReport` и реализовав метод `build(rows)`:

```python
# src/macro_reports/reports/my_report.py
from macro_reports.reports.base import BaseReport

class MyReport(BaseReport):
    def build(self, rows):
        ...
```

2. Зарегистрировать в `src/macro_reports/reports/registry.py`:

```python
from macro_reports.reports.my_report import MyReport

_REPORTS: dict[str, type[BaseReport]] = {
    "average-gdp": AverageGDPReport,
    "my-report": MyReport,       # добавить сюда
}
```

После этого отчёт доступен через `--report my-report` без изменений в CLI.

## Разработка

```bash
make test   # запуск тестов
make cov    # тесты + отчёт о покрытии
make lint   # проверка кода ruff
make fmt    # форматирование кода ruff
```
