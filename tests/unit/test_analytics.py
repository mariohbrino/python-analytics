from pytest import fixture, raises
from src.analytcs.collection import Collection


@fixture
def collection():
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


def test_raise_value_error():
    with raises(
        ValueError,
        match="A filename or data dictionary must be provided.",
    ):
        Collection()


def test_get_dataframe(collection: Collection):
    result = collection.get()
    expected_result = [
        {"id": 1, "name": "Braund, Mr. Owen Harris", "age": 25, "sex": "Male"},
        {"id": 2, "name": "Allen, Mr. William Henry", "age": 35, "sex": "Male"},
        {"id": 3, "name": "Bonnell, Miss. Elizabeth", "age": 58, "sex": "Female"},
        {"id": 4, "name": "Wizz, Mr. William Henry", "age": 25, "sex": "Male"},
        {"id": 5, "name": "Bozz, Miss. Helen", "age": 51, "sex": "Female"},
        {"id": 6, "name": "Gartner, Miss. Lily", "age": 37, "sex": "Female"},
    ]
    assert result.to_dict(orient="records") == expected_result


def test_find_by_name_on_dataframe(collection: Collection):
    result = collection.find(column="name", value="Bonnell, Miss. Elizabeth")
    assert result.isin(["Bonnell, Miss. Elizabeth"]).any().any()


def test_cannot_find_by_name_on_dataframe(collection: Collection):
    result = collection.find(column="name", value="Doe, John")
    assert not result.isin(["Doe, John"]).any().any()
