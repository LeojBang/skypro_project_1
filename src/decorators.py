from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """Декоратор для логирования выполнения функции.

    Аргументы:
        filename (str | None): Имя файла для записи логов. Если None,
        логи выводятся в консоль.

    Возвращает:
        Callable: Обернутая функция с логированием.
    """

    def logging_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: tuple, **kwargs: dict) -> Any:
            """Обертка для логирования начала и конца выполнения функции.

            Аргументы:
                *args: Позиционные аргументы для передаваемой функции.
                **kwargs: Именованные аргументы для передаваемой функции.

            Возвращает:
                Any: Результат выполнения обернутой функции.
            """
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    print(f"{func.__name__} ok")
                else:
                    with open(rf"{filename}", "w", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok\n")
                return result
            except Exception as e:
                if filename is None:
                    print(f"{func.__name__} error: {e.__class__.__name__}. Inputs {args}, {kwargs}")
                else:
                    with open(rf"{filename}", "w", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} error: {e.__class__.__name__}. Inputs {args}, {kwargs}\n")
                raise e

        return wrapper

    return logging_decorator


@log()
def my_function(x: int, y: int) -> int:
    """Суммирует два целых числа.

    Аргументы:
        x (int): Первое целое число.
        y (int): Второе целое число.

    Возвращает:
        int: Сумма двух целых чисел.
    """
    return x + y
