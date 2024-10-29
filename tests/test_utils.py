from unittest.mock import Mock, mock_open, patch

from src.utils import load_transaction


@patch("os.path.exists", return_value=True)  # Патч для проверки существования файла
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="""[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]""",
)
def test_load_transaction_with_data(mock_file: Mock, mock_exist: Mock) -> None:
    expected_data = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    result = load_transaction("true_path.json")
    assert result == expected_data
    mock_file.assert_called_once_with("true_path.json", "r")


@patch("os.path.exists", return_value=False)
@patch("builtins.open", new_callable=mock_open)
def test_load_transaction_nonexistent_file(mock_file: Mock, mock_exist: Mock) -> None:
    """Тест для случая, когда файл не существует."""
    result = load_transaction("fake_path.json")
    assert result == []
    mock_exist.assert_called_once_with("fake_path.json")


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="invalid json")
def test_load_transaction_json_decode_error(mock_file: Mock, mock_exist: Mock) -> None:
    """Тест для случая, когда файл содержит некорректный JSON."""
    result = load_transaction("fake_path.json")
    assert result == []
    mock_file.assert_called_once_with("fake_path.json", "r")


@patch("os.path.exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data='{"key": "value"}')
def test_load_transaction_not_a_list(mock_file: Mock, mock_exist: Mock) -> None:
    result = load_transaction("fake_path.json")
    assert result == []  # ожидаем пустой список, так как данные не список
    mock_file.assert_called_once_with("fake_path.json", "r")
