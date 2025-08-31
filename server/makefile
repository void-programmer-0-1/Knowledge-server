PYTHON=python3
VENV=.venv
PIP=$(VENV)/bin/pip
GUNICORN=$(VENV)/bin/gunicorn
ALEMBIC=$(VENV)/bin/alembic

.PHONY: help init venv install alembic-init alembic-rev alembic-upgrade run test clean

help:
	@echo "Usage:"
	@echo "  make init             Initialize project (venv + install + alembic init)"
	@echo "  make venv             Create virtual environment"
	@echo "  make install          Install dependencies from requirements.txt"
	@echo "  make alembic-init     Initialize Alembic with async engine"
	@echo "  make alembic-rev msg='message'   Generate Alembic revision"
	@echo "  make alembic-upgrade  Run Alembic migrations"
	@echo "  make deploy           Run Gunicorn server (with uvicorn workers)"
	@echo "  make dev              Run Fastapi dev server"
	@echo "  make test             Run tests"
	@echo "  make clean            Remove venv and cache files"

venv:
	$(PYTHON) -m venv $(VENV)

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

alembic-init:
	$(ALEMBIC) init -t async migrations

alembic-rev:
	@if [ -z "${msg}" ]; then \
		echo "Error: Please provide a message. Usage: make alembic-rev msg='message'"; \
		exit 1; \
	fi
	$(ALEMBIC) revision --autogenerate -m "${msg}"

alembic-upgrade:
	$(ALEMBIC) upgrade head

deploy:
	./server.sh

dev:
	fastapi dev server.py

test:
	$(VENV)/bin/pytest

clean:
	rm -rf $(VENV) migrations __pycache__ .pytest_cache

init: venv install alembic-init