.PHONY: fmt lint run migrate rev

fmt:
	poetry run isort .
	poetry run black .

lint:
	poetry run ruff check .

run:
	poetry run uvicorn src.amcp.main:app --reload --host 127.0.0.1 --port 8000

migrate:
	poetry run alembic upgrade head

# usage: make rev m="init schema"
rev:
	poetry run alembic revision --autogenerate -m "$(m)"
