from pandas import DataFrame, read_csv


class DataFrame:
    """
    Class to import csv file and perform operations with pandas library.
    """

    dataframe = None

    def __init__(self, filename=None) -> None:
        """
        Initialize the class with the csv file.
            :param filename: str: Path to the csv file.
        """
        self.dataframe = read_csv(
            filename,
            sep=",",
            skipinitialspace=True,
            header=0,
        )

    def get(self) -> DataFrame:
        """
        Returns the dataframe of the csv file with all data.
        """
        return self.dataframe

    def find(self, column: list[str] | str, value: str) -> DataFrame:
        """
        Find a value in a column of the dataframe.
            :param column: str: Column name to search.
            :param value: str: Value to search.
        """
        return self.dataframe[self.dataframe[column] == value]

    def order_by(self, column: list[str] | str, ascending: bool = True) -> DataFrame:
        """
        Order the dataframe by a column.
            :param column: str: Column name to order.
            :param ascending: bool: Order ascending or descending.
        """
        if ascending:
            return self.dataframe.sort_values(by=column, ascending=True)
        return self.dataframe.sort_values(by=column, ascending=False)

    def group_by(self, column: list[str] | str) -> DataFrame:
        """
        Group the dataframe by a column.
            :param column: str: Column name to group.
        """
        return self.dataframe.groupby(column).size()

    def __str__(self) -> str:
        """
        Return the dataframe as a string.
        """
        return str(self.dataframe)
