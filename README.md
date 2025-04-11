# Python Pandas Example

Create virtual environment and activate. Then, install python dependencies.
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

Run application.
```bash
analyze get --output results/get_results.csv
analyze find --column sex --value Male --output results/filter_results.csv
analyze group_by --columns sex age --output results/group_results.csv
analyze order_by --column age --arrange id age sex name --ascending --output results/order_results.csv
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
