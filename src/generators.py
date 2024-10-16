from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator:
    for transaction in transactions:
        if transaction.get("operationAmount").get("currency").get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Generator:
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator:
    while start != stop + 1 and start <= stop:
        card = f"{str(start):0>16}"
        yield f"{card[:4]} {card[4:8]} {card[8:12]} {card[12:]}"
        start += 1
