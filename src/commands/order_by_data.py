import csv
from typing import List

import click
from pandas import DataFrame

from domains.collection import Collection


@click.command(name="order_by", help="Order data by a column")
@click.option("--filename", help="Input CSV file", default="storage/people.csv")
@click.option("--output", help="Output CSV file", default="results/order_by_results.csv")
@click.option("--columns", help="Columns to order by (comma-separated)", required=True)
@click.option("--arrange", help="Arrange the order by specified criteria (comma-separated)", required=True)
@click.option(
    "--descending",
    help="Sort in descending order (default is ascending)",
    default=False,
    is_flag=True,
)
def order_by_data(
    output: str,
    filename: str,
    columns: str,
    arrange: str,
    descending: bool,
) -> None:
    click.echo(f"Reading data from {filename}")
    collection = Collection(filename=filename)
    click.echo(f"Writing data to '{output}'")
    columns_list: List[str] = columns.split(",")
    arrange_list: List[str] = arrange.split(",") if arrange else []
    results: DataFrame = collection.order_by(
        columns=columns_list,
        arrange=arrange_list,
        ascending=not descending,
    )
    print(results)
    results.to_csv(output, index=False, quoting=csv.QUOTE_ALL)
