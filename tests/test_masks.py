from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number

""" Тестирование правильности маскирования номера карты с применением фикстур и параметризации """


@pytest.mark.parametrize(
    "card, mask_card",
    [
        ("4627100101654724", "4627 10** **** 4724"),
        ("7365410843013587", "7365 41** **** 3587"),
        ("5529263272356119", "5529 26** **** 6119"),
    ],
)
def test_get_mask_card_number(card: str, mask_card: str) -> None:
    assert get_mask_card_number(card) == mask_card


@pytest.mark.parametrize("card", ["462710010165", "46271001016547242345", 2341676, "462d10e10q654724", {}, [], ("3",)])
def test_get_mask_card_number_incorrect(card: str, card_number_incorrect: Any) -> None:
    assert get_mask_card_number(card) == card_number_incorrect


def test_get_mask_card_number_empty(card_number_incorrect: str) -> None:
    assert get_mask_card_number("") == card_number_incorrect


""" Тестирование правильности маскирования номера счета с применением фикстур и параметризации """


@pytest.mark.parametrize(
    "account, mask_account",
    [("73654108430135874305", "**4305"), ("40644687100000002167", "**2167"), ("40893588300000001921", "**1921")],
)
def test_get_mask_account(account: str, mask_account: str) -> None:
    assert get_mask_account(account) == mask_account


@pytest.mark.parametrize("account", ["462710010165", "408935883000000019213423", 234541, "4089s358fe8300A000001921"])
def test_get_mask_account_incorrect(account: str, account_number_incorrect: Any) -> None:
    assert get_mask_account(account) == account_number_incorrect


def test_get_mask_account_is_empty(account_number_incorrect: str) -> None:
    assert get_mask_account("") == account_number_incorrect
