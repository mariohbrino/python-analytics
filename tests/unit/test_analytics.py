from src.analytcs.DataFrame import DataFrame


def test_get_dataframe():
    df = DataFrame(filename="storage/people.csv")
    result = df.get()
    assert result.isin(["Bonnell, Miss. Elizabeth"]).any().any()


def test_find_by_name():
    df = DataFrame(filename="storage/people.csv")
    result = df.find(column="Name", value="Bonnell, Miss. Elizabeth")
    assert result.isin(["Bonnell, Miss. Elizabeth"]).any().any()
