from unittest.mock import Mock, patch

import pytest

from src.file_reader import read_transactions_from_csv, read_transactions_from_excel


@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_pandas: Mock, transactions_cvs_and_excel: list) -> None:
    mock_pandas.return_value.to_dict.return_value = transactions_cvs_and_excel
    result = read_transactions_from_csv("test_path.csv")

    assert result == transactions_cvs_and_excel
    mock_pandas.assert_called_once_with("test_path.csv", delimiter=";")


def test_read_transactions_from_csv_invalid_path() -> None:
    with pytest.raises(FileNotFoundError, match="Файл не найден по указанному пути"):
        read_transactions_from_csv("test_path.csv")


@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_pandas: Mock, transactions_cvs_and_excel: list) -> None:
    mock_pandas.return_value.to_dict.return_value = transactions_cvs_and_excel
    result = read_transactions_from_excel("test_path.xlsx")
    assert result == transactions_cvs_and_excel
    mock_pandas.assert_called_once()


def test_read_transactions_from_excel_invalid_path() -> None:
    with pytest.raises(FileNotFoundError, match="Файл не найден по указанному пути"):
        read_transactions_from_excel("test_path.xlsx")
