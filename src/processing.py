from typing import Dict, List


def filter_by_state(my_list: List[Dict[str, str | int]], state: str = "EXECUTED") -> List[Dict[str, str | int]] | str:
    """Функция принимает и возвращает новый список словарей, у которых ключ state соответствует указанному значению"""
    if not isinstance(my_list, list):
        raise TypeError("my_list должен быть списком словарей")

    for dictionary in my_list:
        if not isinstance(dictionary, dict):
            raise TypeError("Элемент my_list должен быть словарем")
        if "state" not in dictionary:
            raise ValueError("Каждый словарь должен содержать ключ 'state'")

    return [dictionary for dictionary in my_list if dictionary.get("state") == state]


def sort_by_date(my_list: List[Dict[str, str | int]], reverse: bool = True) -> List[Dict[str, str | int]] | str:
    """Функция принимает список словарей и возвращает новый список, отсортированный по дате (date)"""
    try:
        return sorted(my_list, key=lambda x: x["date"], reverse=reverse)
    except TypeError:
        raise TypeError
