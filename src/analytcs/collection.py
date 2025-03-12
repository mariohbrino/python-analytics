from pandas import DataFrame, read_csv


class Collection:
    """
    Class to import csv file and perform operations with pandas library.
    """

    __dataframe: DataFrame | None = None

    def __init__(self, filename: str = None, data: dict[object] = None) -> None:
        """
        Initialize the class with the csv file or data
            :param filename: str: Path to the csv file.
            :param data: dict[object]: Raw data.
            :raises ValueError: If neither filename nor data is provided.
        """
        if filename:
            self.__dataframe = read_csv(
                filename,
                sep=",",
                skipinitialspace=True,
                header=0,
            )
        elif data:
            self.__dataframe = DataFrame(data)
        else:
            raise ValueError("A filename or data dictionary must be provided.")

    def get(self) -> DataFrame:
        """
        Returns the dataframe of the csv file with all data.
        """
        return self.__dataframe

    def find(self, column: list[str] | str, value: str) -> DataFrame:
        """
        Find a value in a column of the dataframe.
            :param column: str: Column name to search.
            :param value: str: Value to search.
        """
        return self.__dataframe[self.__dataframe[column] == value]

    def order_by(
        self, column: list[str] | str, arrange: list[str] = None, ascending: bool = True
    ) -> DataFrame:
        """
        Order the dataframe by a column.
            :param column: str: Column name to order.
            :param arrange: list[str]: Arrange order of columns.
            :param ascending: bool: Order ascending or descending.
        """

        data = self.__dataframe

        if arrange:
            data = data[arrange]
        if ascending:
            return data.sort_values(by=column, ascending=True)
        return data.sort_values(by=column, ascending=False)

    def group_by(self, column: list[str] | str, label: str = "count") -> DataFrame:
        """
        Group the dataframe by a column and add a label for the aggregated column.
            :param column: str: Column name to group.
            :param label: str: Label for the aggregated column.
        """
        return self.__dataframe.groupby(column).size().reset_index(name=label)

    def to_csv(self, *args, **kwargs) -> None:
        """
        Save the dataframe to a csv file.
            :param args: Additional positional arguments for pandas to_csv method.
            :param kwargs: Additional keyword arguments for pandas to_csv method.
        """
        self.__dataframe.to_csv(*args, **kwargs)

    def __str__(self) -> str:
        """
        Return the dataframe as a string.
        """
        return str(self.__dataframe)
