import json
import logging
import os
import re
from collections import Counter
from typing import Any

current_dir = os.path.dirname(os.path.abspath(__file__))

rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transaction(path_to_json: str) -> Any:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.

    :param path_to_json: Путь до JSON-файла с транзакциями.
    :return: Список словарей с данными о транзакциях или пустой список при ошибках.
    """
    logger.info(f"Загружаем данные из {path_to_json}")
    try:
        if not os.path.exists(path_to_json):
            logger.error(f"По указанному пути {path_to_json} файла не существует")
            return []
        with open(path_to_json, "r") as file:
            data = json.load(file)
            if isinstance(data, list) and len(data) != 0:
                logger.info("Данные с файла успешно прочитаны и записаны в data")
                return data
            else:
                logger.error("Внутри файла передан не список словарей")
                return []
    except json.JSONDecodeError as e:
        logger.error(
            f"Декодирование невозможно. Полученные данные не являются JSON-объектом. Ошибка {e}"
        )
        return []


def filter_transaction_by_description(data_operations: list[dict], search_str: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    pattern = re.compile(search_str, re.IGNORECASE)

    return [
        operation
        for operation in data_operations
        if isinstance(operation["state"], str) and re.search(pattern, operation.get("state", ""))
    ]


def counting_transactions_by_type(data_transactions: list[dict], list_category: list) -> dict:
    """Считает количество операций по заданным категориям"""
    category_counts = []

    for transaction in data_transactions:
        if transaction.get("description") in list_category:
            category_counts.append(transaction["description"])

    category_counts_dict = dict(Counter(category_counts))

    return category_counts_dict
