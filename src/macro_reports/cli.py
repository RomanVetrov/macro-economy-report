from __future__ import annotations

import argparse

from macro_reports.loader import load_rows
from macro_reports.render import render_table
from macro_reports.reports.registry import UnknownReportError, get_report


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Формирование отчётов по макроэкономическим данным."
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="Пути к CSV-файлам с данными (можно передать несколько).",
    )
    parser.add_argument(
        "--report",
        required=True,
        help="Название отчёта (например: average-gdp).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        rows = load_rows(args.files)
        report = get_report(args.report)
        result = report.build(rows)
    except FileNotFoundError as e:
        print(str(e))
        return 2
    except UnknownReportError as e:
        print(str(e))
        return 2

    print(render_table(result))
    return 0


def run() -> None:
    raise SystemExit(main())