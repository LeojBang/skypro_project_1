# Widget of Bank Operations

## Цель проекта:
Данный проект предназначен для обработки данных о банковских операциях. Он включает функции для фильтрации операций по статусу, сортировки их по дате, а также для маскирования номеров карт и счетов.

## Установка:

Для установки и управления зависимостями проекта используется Poetry. Убедитесь, что у вас установлена последняя версия Poetry. Если у вас его нет, установите его, следуя [инструкциям на официальном сайте Poetry](https://python-poetry.org/docs/#installation).

- Клонируйте репозиторий:
```
git clone https://github.com/LeojBang/skypro_project_1.git
```
- Установите зависимости проекта:
```
poetry install
pip install -r requirements.txt
```
## Структура проекта

```
│
├── src/                           # Исходный код приложения
│   ├── __init__.py                # Инициализация основного модуля
│   ├── masks.py                   # Модуль с масками данных
│   ├── widget.py                  # Виджет для основной функциональности
│   ├── processing.py              # Модуль для обработки данных
│   └── generators.py              # Модуль содержащий функции, реализующие генераторы для обработки данных.
│
├── tests/                         # Тесты для приложения
│   ├── __init__.py                # Инициализация тестов
│   ├── conftest.py                # Общие фикстуры для тестов
│   ├── test_masks.py              # Тесты для модуля masks.py
│   ├── test_widget.py             # Тесты для виджета widget.py
│   ├── test_widget.py             # Тесты для виджета widget.py
│   ├── test_processing.py         # Тесты для модуля обработки данных processing.py
│   └── generators.py         # Тесты для модуля обработки данных generators.py
│
├── .coverage                      # Файл с результатами покрытия кода
├── .flake8                        # Настройки для проверки качества кода
├── .gitignore                     # Файл, исключающий ненужные файлы из Git
├── main.py                        # Главный файл приложения
├── poetry.lock                    # Файл блокировки зависимостей (Poetry)
├── pyproject.toml                 # Файл настроек проекта и зависимостей (Poetry)
├── README.md                      # Основная документация проекта
└── requirements.txt               # Список зависимостей проекта
```

## Использование:
### Модули
#### 1. processing
- **filter_by_state:** Функция принимает на вход список словарей с данными о банковских операциях и опциональный параметр **state**, который по умолчанию равен 'EXECUTED'. Она возвращает новый список, содержащий только те словари, у которых ключ **state** соответствует указанному значению.
```python
from src.processing import filter_by_state

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
]

executed_operations = filter_by_state(data)
print(executed_operations) # Будет выведено [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
```
 
- **sort_by_date:** Функция принимает список словарей и возвращает новый список, отсортированный по дате (по умолчанию — по убыванию).
```python
from src.processing import sort_by_date

sorted_operations = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
)
```
#### 2. Widget

- **mask_account_card:** Функция принимает имя карты и ее номер или номер счета и возвращает замаскированный вид.

```python
from src.widget import mask_account_card

masked_card = mask_account_card("Visa 1234567812345678")
```
- **get_date**: Функция принимает дату в формате, например, “2024-03-11T02:26:18.671407” и возвращает в формате “ДД.ММ.ГГГГ”.
```python
from src.widget import get_date

formatted_date = get_date("2024-03-11T02:26:18.671407")
```
#### 3. Masks

- **get_mask_card_number**: Функция принимает номер карты и возвращает маску его.

```python
from src.masks import get_mask_card_number

masked_card_number = get_mask_card_number("1234567812345678")
```
- **get_mask_account**: Функция принимает номер счета и маскирует его.
```python
from src.masks import get_mask_account

masked_account_number = get_mask_account("12345678901234567890")
```
#### 3. Generators

- **filter_by_currency**: Функция, которая принимает на вход список словарей, представляющих транзакции.
Функция возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)..

```python
from src.generators import filter_by_currency

transactions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }]
usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(1):
    print(next(usd_transactions))
```
- **transaction_descriptions**: Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
```python
from src.generators import transaction_descriptions

transactions = [{
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
        "amount": "9824.07",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
}]
descriptions = transaction_descriptions(transactions)
for _ in range(1):
    print(next(descriptions))
```
- **card_number_generator**: Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
```python
from src.generators import card_number_generator

for card_number in card_number_generator(3, 3):
    print(card_number) # 0000 0000 0000 0003
```

## Тестирование
Для Запуска тестов используйте команду
`pytest`
## Документация

### Описание проекта
Widget of Bank Operations предназначен для обработки и маскирования данных о банковских операциях. Он позволяет фильтровать операции по статусу, сортировать их по дате и скрывать конфиденциальные данные, такие как номера карт и счетов.

### Контакты
Для вопросов и предложений, пожалуйста, свяжитесь со мной по электронной почте: m.merkulovdodo@gmail.com
## Источники
### Skypro
