from argparse import ArgumentParser
from logging import basicConfig, INFO, getLogger
import csv
from analytcs.collection import Collection

basicConfig(level=INFO)
logger = getLogger(__name__)


def main():
    parser = ArgumentParser(description="Analytics CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcommand: get
    get_parser = subparsers.add_parser("get", help="Retrieve all data")
    get_parser.add_argument("--output", help="Output CSV file", required=True)

    # Subcommand: find
    find_parser = subparsers.add_parser("find", help="Filter data by column and value")
    find_parser.add_argument("--column", help="Column to filter by", required=True)
    find_parser.add_argument("--value", help="Value to filter by", required=True)
    find_parser.add_argument("--output", help="Output CSV file", required=True)

    # Subcommand: group_by
    group_parser = subparsers.add_parser("group_by", help="Group data by columns")
    group_parser.add_argument(
        "--columns", nargs="+", help="Columns to group by", required=True
    )
    group_parser.add_argument("--output", help="Output CSV file", required=True)

    # Subcommand: order_by
    order_parser = subparsers.add_parser("order_by", help="Order data by a column")
    order_parser.add_argument("--column", help="Column to order by", required=True)
    order_parser.add_argument(
        "--arrange", nargs="+", help="Columns arrangement", required=True
    )
    order_parser.add_argument(
        "--ascending", action="store_true", help="Sort in ascending order"
    )
    order_parser.add_argument("--output", help="Output CSV file", required=True)

    args = parser.parse_args()

    # Initialize the collection
    collection = Collection(filename="storage/people.csv")

    # Handle commands
    match args.command:
        case "get":
            results = collection.get()
            print(results)
            results.to_csv(args.output, index=False, quoting=csv.QUOTE_ALL)

        case "find":
            results = collection.find(column=args.column, value=args.value)
            print(results)
            results.to_csv(args.output, index=False, quoting=csv.QUOTE_ALL)

        case "group_by":
            results = collection.group_by(column=args.columns)
            print(results)
            results.to_csv(args.output, index=False, quoting=csv.QUOTE_ALL)

        case "order_by":
            results = collection.order_by(
                column=args.column, arrange=args.arrange, ascending=args.ascending
            )
            print(results)
            results.to_csv(args.output, index=False, quoting=csv.QUOTE_ALL)


if __name__ == "__main__":
    main()
