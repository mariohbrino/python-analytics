.DEFAULT_GOAL = help

help: # Show a list of commands available.
	@echo "List of commands to work with Laravel environment."
	@echo "usage: make <command>\n"
	@echo "Commands:\n"
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

setup: # Set up virtual environment.
	@python3 -m venv .venv

install: # Install dependencies.
	@pip install -e .

lint: # Run python linting format.
	@ruff format .

test: # Run all tests.
	@python -m pytest -v

coverage: # Run all tests with coverage.
	@python -m pytest -v --cov-report term-missing --cov --cov-fail-under=95
