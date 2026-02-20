from macro_reports.cli import main


def test_cli_unknown_report_prints_message(capsys, tmp_path) -> None:
    # создаём минимальный валидный csv, чтобы ошибка была именно про report, а не про файл
    data_file = tmp_path / "data.csv"
    data_file.write_text(
        "country,year,gdp\nUSA,2023,10\n",
        encoding="utf-8",
    )

    code = main(["--files", str(data_file), "--report", "no-such-report"])
    captured = capsys.readouterr()

    assert code == 2
    assert "Неизвестный отчёт" in captured.out
