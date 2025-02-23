import logging
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и возвращает маску его"""
    logger.info(f"Попытка маскировки карты {card_number}")
    if isinstance(card_number, str) and card_number.isdigit() and len(card_number) == 16:
        logger.info("Маскировка карты успешно завершена")
        return f"{card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]}"
    logger.error("Ошибка выполнения. Передан неверный формат номера карты")
    return "Номер карты некорректен"


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета и маскирует его"""
    logger.info(f"Попытка маскировки счета {account_number}")
    if isinstance(account_number, str) and account_number.isdigit() and len(account_number) == 20:
        logger.info("Маскировка номера карты успешно завершена")
        return "**" + account_number[-4:]
    logger.error("Ошибка выполнения. Передан неверный формат номера счета")
    return "Номер счета некорректен"
