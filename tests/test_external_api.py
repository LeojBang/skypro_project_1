import os
from unittest.mock import Mock, patch

from dotenv import load_dotenv

from src.external_api import convert_transaction_amount_to_rub

# Загрузка переменных окружения
load_dotenv()
HEADERS = {"apikey": os.getenv("API_KEY")}
URL_TO_CONVERT = "https://api.apilayer.com/exchangerates_data/latest?symbols=USD%2CEUR&base=RUB"


@patch("requests.request")
def test_convert_transaction_amount_to_rub(mock_get: Mock, operation_usd: dict) -> None:
    mock_response = Mock()
    mock_response.json.return_value = {
        "success": True,
        "timestamp": 1730186522,
        "base": "RUB",
        "date": "2024-10-29",
        "rates": {"USD": 0.010283, "EUR": 0.00951},
    }
    mock_get.return_value = mock_response
    assert convert_transaction_amount_to_rub(operation_usd) == 3107807.0601964407
    mock_get.assert_called_once_with("GET", URL_TO_CONVERT, headers=HEADERS)


def test_without_requests_convert_transaction_amount_to_rub(operation_rub: dict) -> None:
    assert convert_transaction_amount_to_rub(operation_rub) == 31957.58
