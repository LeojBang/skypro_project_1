import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_correct(filter_by_state_correct: list[dict[str, str | int]]) -> None:
    assert (
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
        )
        == filter_by_state_correct
    )


@pytest.mark.parametrize(
    "value, state, expected",
    [
        ("", "", "Ошибка ввода"),
        (12345, 567, "Ошибка ввода"),
        (12345, "", "Ошибка ввода"),
    ],
)
def test_filter_by_state(value: list, state: str, expected: list) -> None:
    with pytest.raises(TypeError):
        filter_by_state(value, state)


def test_sort_by_date_reverse(sort_by_date_correct: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == sort_by_date_correct
    )


def test_sort_by_date_not_reverse(sort_by_date_correct: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        )
        == sort_by_date_correct[::-1]
    )


@pytest.mark.parametrize(
    "value, reverse, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
            False,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_equal_dates(value: list, reverse: bool, expected: list) -> None:
    assert sort_by_date(value, reverse) == expected


def test_sort_by_date_invalid(invalid_data: list) -> None:
    with pytest.raises(TypeError):
        sort_by_date(invalid_data)
