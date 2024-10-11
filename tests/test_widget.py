import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_correct(card_correct: str) -> None:
    assert mask_account_card("Счет 73654108430135874305") == card_correct


def test_mask_card_correct(account_correct: str) -> None:
    assert mask_account_card("Visa Classic 4000000000000002") == account_correct


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Classic 4000000000000002", "Visa Classic 4000 00** **** 0002"),
        ("Maestro 5000000000000004", "Maestro 5000 00** **** 0004"),
        ("MasterCard 5100000000000004", "MasterCard 5100 00** **** 0004"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Unknown Card 7000792289606361", "Номер карты или счета не корректен"),
        ("", "Номер карты или счета не корректен"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


def test_get_date_correct(data_correct: str) -> None:
    assert get_date("2024-03-11T02:26:18.671407") == data_correct


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-02-20T12:00:00.000000", "20.02.2023"),
        ("", "Некорректная дата"),
        (" ", "Некорректная дата"),
        (132, "Некорректная дата"),
        ("Jnsaj7672", "Некорректная дата"),
        ("2024-03-11T02:26", "11.03.2024"),
    ],
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected
