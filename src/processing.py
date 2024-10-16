from typing import Dict, List

from src.widget import get_date


def filter_by_state(my_list: List[Dict[str, str | int]], state: str = "EXECUTED") -> List[Dict[str, str | int]] | str:
    """Функция принимает и возвращает новый список словарей, у которых ключ state соответствует указанному значению"""
    if isinstance(my_list, list):
        return [dictionary for dictionary in my_list if dictionary.get("state") == state]
    raise TypeError("Ошибка ввода")


def sort_by_date(my_list: List[Dict[str, str | int]], reverse: bool = True) -> List[Dict[str, str | int]] | str:
    """Функция принимает список словарей и возвращает новый список, отсортированный по дате (date)"""
    try:
        return sorted(my_list, key=lambda x: x["date"], reverse=reverse)
    except TypeError:
        raise TypeError

