def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты и возвращает маску его"""
    if isinstance(card_number, str) and card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4] + ' ' + card_number[4:6] + '** **** ' + card_number[-4:]}"
    else:
        return "Номер карты должен состоять только из строки цифр и быть длинной в 16 символов"


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета и маскирует его"""
    if isinstance(account_number, str) and account_number.isdigit() and len(account_number) == 20:
        return "**" + account_number[-4:]
    else:
        return "Номер счета должен состоять из строки цифр и быть длинной в 20 символов"
