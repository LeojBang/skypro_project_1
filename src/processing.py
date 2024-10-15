from typing import Dict, List

from src.widget import get_date


def filter_by_state(my_list: List[Dict[str, str | int]], state: str = "EXECUTED") -> List[Dict[str, str | int]] | str:
    """Функция принимает и возвращает новый список словарей, у которых ключ state соответствует указанному значению"""
    if isinstance(my_list, list):
        return [dictionary for dictionary in my_list if dictionary.get("state") == state]
    return "Ошибка ввода"


def sort_by_date(my_list: List[Dict[str, str | int]], reverse: bool = True) -> List[Dict[str, str | int]] | str:
    """Функция принимает список словарей и возвращает новый список, отсортированный по дате (date)"""
    for item in my_list:
        if "date" not in item or get_date(item["date"]) == "Некорректная дата":
            return "Некорректная дата"

    return sorted(my_list, key=lambda x: x["date"], reverse=reverse)
