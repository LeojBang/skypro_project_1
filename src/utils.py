import json
import os
from typing import Any


def load_transaction(path_to_json: str) -> Any:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.

    :param path_to_json: Путь до JSON-файла с транзакциями.
    :return: Список словарей с данными о транзакциях или пустой список при ошибках.
    """
    try:
        if not os.path.exists(path_to_json):
            return []
        with open(path_to_json, "r") as file:
            data = json.load(file)
            if isinstance(data, list) and len(data) != 0:
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []
