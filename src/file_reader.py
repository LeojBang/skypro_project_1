import pandas as pd


def read_transactions_from_csv(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    try:
        data_csv = pd.read_csv(file_path, delimiter=";")
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден по указанному пути")
    data_csv_to_dict = data_csv.to_dict(orient="records")
    return data_csv_to_dict


def read_transactions_from_excel(file_path: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""
    try:
        data_excel = pd.read_excel(file_path)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден по указанному пути")
    data_excel_to_dict = data_excel.to_dict(orient="records")
    return data_excel_to_dict
