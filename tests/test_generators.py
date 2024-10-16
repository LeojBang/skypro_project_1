import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "expected",
    [
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            },
        ]
    ],
)
def test_filter_by_currency_usd(transactions: list, expected: list) -> None:
    result = list(filter_by_currency(transactions, "USD"))  # Собираем все результаты в список
    assert result == list(expected)


def test_filter_by_currency_rub(transactions: list) -> None:
    result = list(filter_by_currency(transactions, "RUB"))
    expected = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    assert result == expected


def test_transaction_descriptions(transactions: list) -> None:
    result = list(transaction_descriptions(transactions))
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert result == expected


def test_transaction_descriptions_empty() -> None:
    result = list(transaction_descriptions([]))
    expected: list = []
    assert result == expected


def test_card_number_generator_correct_format() -> None:
    gen = card_number_generator(1, 5)
    expected_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

    for expected in expected_numbers:
        assert next(gen) == expected


def test_card_number_generator_edge_values() -> None:
    gen_start = card_number_generator(0, 0)
    assert next(gen_start) == "0000 0000 0000 0000"

    gen_end = card_number_generator(9999999999999999, 9999999999999999)
    assert next(gen_end) == "9999 9999 9999 9999"


def test_card_number_generator_empty_range() -> None:
    gen_empty = card_number_generator(5, 1)
    assert list(gen_empty) == []


def test_card_number_generator_large_range() -> None:
    gen = card_number_generator(9990000000000000, 9990000000000005)
    expected_numbers = [
        "9990 0000 0000 0000",
        "9990 0000 0000 0001",
        "9990 0000 0000 0002",
        "9990 0000 0000 0003",
        "9990 0000 0000 0004",
    ]

    for expected in expected_numbers:
        assert next(gen) == expected
