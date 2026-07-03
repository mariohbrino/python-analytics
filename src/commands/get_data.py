import csv

import click
from pandas import DataFrame

from domains.collection import Collection


@click.command(name="get", help="Retrieve all data")
@click.option("--output", help="Output CSV file", required=True)
@click.option("--filename", help="Input CSV file", default="storage/people.csv")
def get_data(
    output: str,
    filename: str,
) -> None:
    click.echo(f"Reading data from {filename}")
    collection = Collection(filename=filename)
    click.echo(f"Writing data to '{output}'")
    results: DataFrame = collection.get()
    print(results)
    results.to_csv(output, index=False, quoting=csv.QUOTE_ALL)
