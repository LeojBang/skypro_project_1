import json
import logging
import os
from typing import Any

# Настройка логера для utils.log
load_transaction_logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s = - %(name)s - %(levelname)s - %(message)s"))

# Добавляем обработчик к логеру
load_transaction_logger.addHandler(file_handler)
load_transaction_logger.setLevel(logging.DEBUG)


def load_transaction(path_to_json: str) -> Any:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.
    Если файл пустой, содержит не список или не найден, возвращает пустой список.

    :param path_to_json: Путь до JSON-файла с транзакциями.
    :return: Список словарей с данными о транзакциях или пустой список при ошибках.
    """
    load_transaction_logger.info(f"Загружаем данные из {path_to_json}")
    try:
        if not os.path.exists(path_to_json):
            load_transaction_logger.error(f"По указанному пути {path_to_json} файла не существует")
            return []
        with open(path_to_json, "r") as file:
            data = json.load(file)
            if isinstance(data, list) and len(data) != 0:
                load_transaction_logger.info("Данные с файла успешно прочитаны и записаны в data")
                return data
            else:
                load_transaction_logger.error("Внутри файла передан не список словарей")
                return []
    except json.JSONDecodeError as e:
        load_transaction_logger.error(
            f"Декодирование невозможно. Полученные данные не являются JSON-объектом. Ошибка {e}"
        )
        return []
