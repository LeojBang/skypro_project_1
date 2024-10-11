import pytest


@pytest.fixture
def card_number_incorrect() -> str:
    return "Номер карты некорректен"


@pytest.fixture
def account_number_incorrect() -> str:
    return "Номер счета некорректен"


@pytest.fixture
def account_correct() -> str:
    return "Visa Classic 4000 00** **** 0002"


@pytest.fixture
def card_correct() -> str:
    return "Счет **4305"


@pytest.fixture
def data_correct() -> str:
    return "11.03.2024"


@pytest.fixture
def filter_by_state_correct() -> list[dict[str, str | int]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort_by_date_correct() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def equal_dates() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def invalid_data() -> list:
    return [
        {"id": 1, "state": "EXECUTED", "date": ""},
        {"id": 2, "state": "EXECUTED", "date": "invalid_date"},
        {"id": 3, "state": "EXECUTED", "date": None},
        {"id": 4, "state": "EXECUTED", "date": 123456},
    ]
