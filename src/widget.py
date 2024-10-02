from src import masks


def mask_account_card(account_card: str) -> str:
    """Функция принимает имя карты и ее номер или номер счета и возвращает замаскированный вид"""
    if len(account_card.split()[-1]) == 16:
        return f"{' '.join(account_card.split()[:-1])} {masks.get_mask_card_number(account_card.split()[-1])}"
    elif len(account_card.split()[-1]) == 20:
        return f"{' '.join(account_card.split()[:-1])} {masks.get_mask_account(account_card.split()[-1])}"
    return "Номер карты должен состоять из 16 цифр, а номер счета из 20 цифр"


def get_date(date: str) -> str:
    """Функция принимает дату в формате, например, "2024-03-11T02:26:18.671407" и возвращает в формате "ДД.ММ.ГГГГ" """
    year, month, day = date.split("T")[0].split("-")
    return f"{day}.{month}.{year}"
