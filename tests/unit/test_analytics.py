import csv
import os
from pytest import fixture, raises
from analytcs.collection import Collection


@fixture
def collection() -> Collection:
    data = {
        "id": [1, 2, 3, 4, 5, 6],
        "name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
            "Wizz, Mr. William Henry",
            "Bozz, Miss. Helen",
            "Gartner, Miss. Lily",
        ],
        "age": [25, 35, 58, 25, 51, 37],
        "sex": ["Male", "Male", "Female", "Male", "Female", "Female"],
    }
    return Collection(data=data)


@fixture
def expected_result() -> list[object]:
    return [
        {"id": 1, "name": "Braund, Mr. Owen Harris", "age": 25, "sex": "Male"},
        {"id": 2, "name": "Allen, Mr. William Henry", "age": 35, "sex": "Male"},
        {"id": 3, "name": "Bonnell, Miss. Elizabeth", "age": 58, "sex": "Female"},
        {"id": 4, "name": "Wizz, Mr. William Henry", "age": 25, "sex": "Male"},
        {"id": 5, "name": "Bozz, Miss. Helen", "age": 51, "sex": "Female"},
        {"id": 6, "name": "Gartner, Miss. Lily", "age": 37, "sex": "Female"},
    ]


def test_raise_value_error():
    with raises(
        ValueError,
        match="A filename or data dictionary must be provided.",
    ):
        Collection()


def test_import_csv_file(collection: Collection, expected_result: list[object]):
    collection.to_csv("results/people.csv", index=False, quoting=csv.QUOTE_ALL)
    data = Collection(filename="results/people.csv")
    result = data.get()
    assert result.to_dict(orient="records") == expected_result


def test_get_dataframe(collection: Collection, expected_result: list[object]):
    result = collection.get()
    assert result.to_dict(orient="records") == expected_result


def test_find_by_name_on_dataframe(collection: Collection):
    result = collection.find(column="name", value="Bonnell, Miss. Elizabeth")
    assert result.isin(["Bonnell, Miss. Elizabeth"]).any().any()


def test_cannot_find_by_name_on_dataframe(collection: Collection):
    result = collection.find(column="name", value="Doe, John")
    assert not result.isin(["Doe, John"]).any().any()


def test_order_by_assending_dataframe(collection: Collection):
    result = collection.order_by(column="name", ascending=True)
    assert result.iloc[0]["name"] == "Allen, Mr. William Henry"


def test_order_by_dessending_dataframe(collection: Collection):
    result = collection.order_by(column="name", ascending=False)
    assert result.iloc[0]["name"] == "Wizz, Mr. William Henry"


def test_order_by_with_arrange_dataframe(collection: Collection):
    result = collection.order_by(
        column="name", arrange=["id", "age", "sex", "name"], ascending=False
    )
    assert result.iloc[0]["name"] == "Wizz, Mr. William Henry"


def test_group_by_sex_and_age(collection: Collection):
    result = collection.group_by(column=["sex", "age"])
    expected_result = [
        {"sex": "Female", "age": 37, "count": 1},
        {"sex": "Female", "age": 51, "count": 1},
        {"sex": "Female", "age": 58, "count": 1},
        {"sex": "Male", "age": 25, "count": 2},
        {"sex": "Male", "age": 35, "count": 1},
    ]
    assert result.to_dict(orient="records") == expected_result


def test_generate_csv_report(collection: Collection):
    result = collection.get()
    os.makedirs("results", exist_ok=True)
    result.to_csv("results/report.csv", index=False, quoting=csv.QUOTE_ALL)
    assert os.path.exists("results/report.csv")


def test_collection_str_method(collection: Collection):
    expected_str = str(collection)
    assert str(collection) == expected_str
