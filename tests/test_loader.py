from pathlib import Path

import pytest

from macro_reports.loader import load_rows


def test_load_rows_reads_and_merges_multiple_files(tmp_path: Path) -> None:
    """позитивный сценарий"""
    file1 = tmp_path / "a.csv"
    file2 = tmp_path / "b.csv"

    file1.write_text(
        "country,year,gdp\nUSA,2023,10\nChina,2023,20\n",
        encoding="utf-8",
    )
    file2.write_text(
        "country,year,gdp\nUSA,2022,30\n",
        encoding="utf-8",
    )

    rows = load_rows([str(file1), str(file2)])

    assert len(rows) == 3
    assert rows[0]["country"] == "USA"
    assert rows[1]["country"] == "China"
    assert rows[2]["year"] == "2022"
    assert rows[2]["gdp"] == "30"


def test_load_rows_raises_if_file_not_found(tmp_path: Path) -> None:
    """негативный сценарий"""
    missing = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError) as exc:
        load_rows([str(missing)])

    assert "Файл не найден" in str(exc.value)
