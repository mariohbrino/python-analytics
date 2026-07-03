import csv

import click
from pandas import DataFrame

from domains.collection import Collection


@click.command(name="find", help="Filter data by column and value")
@click.option("--filename", help="Input CSV file", default="storage/people.csv")
@click.option("--output", help="Output CSV file", default="results/filter_results.csv")
@click.option("--column", help="Column to search", required=True)
@click.option("--value", help="Value to search for", required=True)
def find_data(
    output: str,
    filename: str,
    column: str,
    value: str,
) -> None:
    click.echo(f"Reading data from {filename}")
    collection = Collection(filename=filename)
    click.echo(f"Writing data to '{output}'")
    results: DataFrame = collection.find(columns=column, value=value)
    print(results)
    results.to_csv(output, index=False, quoting=csv.QUOTE_ALL)
