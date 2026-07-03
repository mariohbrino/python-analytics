# Python Pandas Example

## Set Up Environment

Install UV package managment
```bash
pip install uv
```

Create virtual environment and activate. Then, install project in editable mode.
```bash
uv sync
source .venv/bin/activate
pip install -e .
```

## CLI Usage

Run application.
```bash
analyze get --output results/get_results.csv
analyze find --column sex --value Male --output results/filter_results.csv
analyze group_by --columns "sex,age" --output results/group_results.csv
analyze order_by --columns age --arrange "id,age,sex,name" --output results/order_results.csv
```

## Development

Linting check and format for python using Ruff.
```bash
ruff check .
ruff format .
```

## Testing

Run tests.
```bash
python -m pytest -v --cov-report term-missing --cov --cov-fail-under=95
```

> Use flag `--cov` to show test coverage.
