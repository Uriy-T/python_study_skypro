from typing import Any

from config import available_states

log_valid_data: list[dict[str, Any]] = [
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ],
        "state": "EXECUTED",
        "log_data": "Функция: filter_by_state - успешно.\n"
                    "Результат работы:\n"
                    "[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]\n\n"
    }
]

invalid_dataset: list[dict[str, Any]] = [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
            },
            {
                "id": 615064591,
                "state": "CANCELED",
                "date": "2018-10-14T08:21:33.419441",
            },
        ]
log_invalid_data: list[dict[str, Any]] = [
    {
        "data_for_filter": invalid_dataset,
        "state": "AWAIT",
        "log_data":
            "Функция: filter_by_state - ошибка выполнения.\n"
            "Результат работы:\n"
            "Значения state нет в списке доступных состояний."
            f"Доступны: {available_states}\n"
            f"Были введены данные: ({invalid_dataset!r},), {{'state': 'AWAIT'}}\n\n",
    }
]
