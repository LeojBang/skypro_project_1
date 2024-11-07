import os

import requests
from dotenv import load_dotenv

load_dotenv()
HEADERS = {"apikey": os.getenv("API_KEY")}
URL_TO_CONVERT = os.getenv("URL_TO_CONVERT")


def convert_transaction_amount_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли. Если валюта транзакции USD или EUR,
    использует API для получения курса и конвертации в рубли.
    """
    amount = float(transaction["operationAmount"]["amount"])
    code = transaction["operationAmount"]["currency"]["code"]

    if code in ["USD", "EUR"] and URL_TO_CONVERT is not None:
        response = requests.request("GET", url=URL_TO_CONVERT, headers=HEADERS)
        rate = response.json()["rates"][code]

        return float(amount / rate)
    return float(amount)
