import csv

import click
from pandas import DataFrame

from domains.collection import Collection


@click.command(name="group_by", help="Group data by columns")
@click.option("--filename", help="Input CSV file", default="storage/people.csv")
@click.option("--output", help="Output CSV file", default="results/group_by_results.csv")
@click.option("--columns", help="Columns to group by (comma-separated)", required=True)
def group_by_data(
    output: str,
    filename: str,
    columns: str,
) -> None:
    click.echo(f"Reading data from {filename}")
    collection = Collection(filename=filename)
    click.echo(f"Writing data to '{output}'")
    columns_list = columns.split(",")
    results: DataFrame = collection.group_by(columns=columns_list)
    print(results)
    results.to_csv(output, index=False, quoting=csv.QUOTE_ALL)
