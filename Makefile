test:
	uv run pytest

cov:
	uv run pytest --cov=macro_reports --cov-report=term-missing

lint:
	uv run ruff check .

fmt:
	uv run ruff format .

# alias, чтобы привычно было писать make format
format: fmt

check: lint test cov

clean:
	rm -rf .pytest_cache .ruff_cache .coverage htmlcov coverage.xml
	find . -type d -name "__pycache__" -prune -exec rm -rf {} \;