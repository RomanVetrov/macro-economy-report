from __future__ import annotations

import sys

from macro_reports.cli import main


if __name__ == "__main__":
    #отрезаем имя скрипта и передаём аргументы в мейн
    raise SystemExit(main(sys.argv[1:]))
