import pytest


@pytest.fixture(scope="module")
def some_list_data():
    """Fixture that returns some list data"""
    print("before")
    yield [1, 2, 3, 4, 5]
    print("after")


@pytest.fixture()
def some_dict_data():
    """Fixture that returns dict data"""
    return {
        "name": "John",
        "lastname": "Wick",
        "age": 44,
        "job": "Accountant"
    }

def test_one(some_list_data):
    assert some_list_data == [1, 2, 3, 4, 5]

def test_one_len(some_list_data):
    assert len(some_list_data) == 5

def test_two(some_dict_data):
    name = some_dict_data.get("name")
    lastname = some_dict_data.get("lastname")
    age = some_dict_data.get("age")
    job = some_dict_data.get("job")
    assert name == "John"
    assert lastname == "Wick"
    assert age == 44
    assert job == "Accountant"

def test_mix(some_list_data, some_dict_data):
    assert some_list_data[4] == 5
    assert some_dict_data.get("name") == "John"