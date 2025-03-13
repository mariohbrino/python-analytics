# Python Pandas Example

Create virtual environment and activate. Then, install python dependencies.
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run application.
```bash
python main.py
```

Linting check and format for python using Ruff.
```bash
ruff check .
ruff format .
```

Run tests.
```bash
python -m pytest -v --cov-report term-missing --cov --cov-fail-under=95
```

> Use flag `--cov` to show test coverage.
