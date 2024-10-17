from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция принимает имя карты и ее номер или номер счета и возвращает замаскированный вид"""
    card_types = ["Visa Classic", "Visa Gold", "Visa Platinum", "Maestro", "MasterCard"]
    for card_type in card_types:
        if card_type in account_card:
            card_number = account_card.split()[-1]
            return f"{card_type} {get_mask_card_number(card_number)}"
    if "Счет" in account_card:
        account_number = account_card.split()[-1]
        return f"{account_card.split()[0]} {get_mask_account(account_number)}"
    else:
        return "Номер карты или счета не корректен"


def get_date(date: str) -> str:
    if not isinstance(date, str):
        raise ValueError("Ожидается строка, но был передан другой тип данных")
    try:
        return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")
