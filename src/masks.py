import logging

# Настройка единого логера для masks.log
masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter("%(asctime)s = - %(name)s - %(levelname)s - %(message)s"))

# Добавляем обработчик к логеру
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и возвращает маску его"""
    masks_logger.info(f"Попытка маскировки карты {card_number}")
    if isinstance(card_number, str) and card_number.isdigit() and len(card_number) == 16:
        masks_logger.info("Маскировка карты успешно завершена")
        return f"{card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]}"
    masks_logger.error("Ошибка выполнения. Передан неверный формат номера карты")
    return "Номер карты некорректен"


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета и маскирует его"""
    masks_logger.info(f"Попытка маскировки счета {account_number}")
    if isinstance(account_number, str) and account_number.isdigit() and len(account_number) == 20:
        masks_logger.info("Маскировка номера карты успешно завершена")
        return "**" + account_number[-4:]
    masks_logger.error("Ошибка выполнения. Передан неверный формат номера счета")
    return "Номер счета некорректен"
