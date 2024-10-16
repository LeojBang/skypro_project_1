import os

import pytest
from pytest import CaptureFixture

from src.decorators import log, my_function


def test_my_function_raises_type_error() -> None:
    with pytest.raises(TypeError):
        my_function("1", 2)


def test_my_function_success(capsys: CaptureFixture) -> None:
    """Тестируем совпадает ли вывод в консоль с выводом декоратора"""
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"


def test_my_function_logs_success_to_file() -> None:
    log_file = os.path.abspath("test_log.txt")  # Создаем временный файл для логов
    my_function_with_logging = log(filename=str(log_file))(my_function)

    # Вызов функции с корректными данными
    my_function_with_logging(1, 2)

    # Открываем файл в режиме чтения и проверяем, что лог записан
    with open(log_file, "r", encoding="utf-8") as file:
        assert file.read() == "my_function ok\n"  # Проверяем правильность записи в файл


def test_my_function_logs_error_to_file() -> None:
    log_file = os.path.abspath("test_log.txt")  # Создаем временный файл для логов
    my_function_with_logging = log(filename=str(log_file))(my_function)

    # Вызов функции с корректными данными
    with pytest.raises(TypeError):
        my_function_with_logging(1, "2")

    # Открываем файл и проверяем, что ошибка логируется корректно
    with open(log_file, "r", encoding="utf-8") as file:
        text = file.read()
        assert text == "my_function error: TypeError. Inputs (1, '2'), {}\n"  # Проверка логируемых входных данных
