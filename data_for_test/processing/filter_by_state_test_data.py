from typing import Any

fbs_valid_data: list[dict[str, Any]] = [
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
        "filtered_list": [
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
        ],
    },
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
        "state": "CANCELED",
        "filtered_list": [
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
    },
]

fbs_valid_data_partial: list[dict[str, Any]] = [
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
        "filtered_list": [
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
        ],
    }
]

fbs_invalid_data: list[dict[str, Any]] = [
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
        "state": "AWAIT",
        "system_answer": "Значения state нет в списке доступных состояний."
        "Доступны: ['EXECUTED', 'CANCELED']",
        "exception_type": ValueError,
    },
    {
        "data_for_filter": [],
        "state": "EXECUTED",
        "system_answer": "Данные для обработки не предоставлены.",
        "exception_type": ValueError,
    },
    {
        "data_for_filter": [{}],
        "state": "EXECUTED",
        "system_answer": "Данные для обработки не предоставлены.",
        "exception_type": ValueError,
    },
    {
        "data_for_filter": {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
        },
        "state": "EXECUTED",
        "system_answer": "data_for_filter должен быть list."
        "Получен тип: dict",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": (
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            },
        ),
        "state": "EXECUTED",
        "system_answer": "data_for_filter должен быть list."
        "Получен тип: tuple",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": {41428829, 594226727},
        "state": "EXECUTED",
        "system_answer": "data_for_filter должен быть list."
        "Получен тип: set",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            },
            [594226727, "CANCELED", "2018-09-12T21:27:25.241689"],
        ],
        "state": "EXECUTED",
        "system_answer": "Все элементы data_for_filter должны быть dict",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            },
            {594226727, "CANCELED", "2018-09-12T21:27:25.241689"},
        ],
        "state": "EXECUTED",
        "system_answer": "Все элементы data_for_filter должны быть dict",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            },
            (594226727, "CANCELED", "2018-09-12T21:27:25.241689"),
        ],
        "state": "EXECUTED",
        "system_answer": "Все элементы data_for_filter должны быть dict",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter"
        "отсутствует ключ: id",
        "exception_type": KeyError,
    },
    {
        "data_for_filter": [
            {"id": 41428829, "date": "2019-07-03T18:35:29.512364"}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter"
        "отсутствует ключ: state",
        "exception_type": KeyError,
    },
    {
        "data_for_filter": [{"id": 41428829, "state": "EXECUTED"}],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter"
        "отсутствует ключ: date",
        "exception_type": KeyError,
    },
    {
        "data_for_filter": [
            {
                "id": "41428829",
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа id не является int",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 4142882.9,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа id не является int",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": [1, 2, 3],
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа id не является int",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": {"prefix": "invest", "number_id": 18762246},
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа id не является int",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": {"invest", 18762246},
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа id не является int",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": (1, 2, 3),
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа id не является int",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": None,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа id не является int",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": True,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа id не является int",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {"id": 41428829, "state": 1, "date": "2019-07-03T18:35:29.512364"}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа state не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": 1.14,
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа state не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": False,
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа state не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": None,
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа state не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": ["pre", "execute"],
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа state не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": {"additional": "pre", "base": "execute"},
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа state не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": {"pre", "execute"},
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа state не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": ("pre", "execute"),
                "date": "2019-07-03T18:35:29.512364",
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа state не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {"id": 41428829, "state": "EXECUTED", "date": "3T18:35:29.512364"}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа date не является форматом ISO",
        "exception_type": ValueError,
    },
    {
        "data_for_filter": [{"id": 41428829, "state": "EXECUTED", "date": 54}],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа date не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {"id": 41428829, "state": "EXECUTED", "date": 76.1}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа date не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {"id": 41428829, "state": "EXECUTED", "date": True}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа date не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {"id": 41428829, "state": "EXECUTED", "date": None}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа date не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {"id": 41428829, "state": "EXECUTED", "date": [12, 7, 2023]}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа date не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {"id": 41428829, "state": "EXECUTED", "date": (12, 7, 2023)}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа date не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {"id": 41428829, "state": "EXECUTED", "date": {12, 7, 2023}}
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа date не является str",
        "exception_type": TypeError,
    },
    {
        "data_for_filter": [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": {"day": 12, "month": 7, "year": 2023},
            }
        ],
        "state": "EXECUTED",
        "system_answer": "В одном или более элементах data_for_filter,"
        "значение ключа date не является str",
        "exception_type": TypeError,
    },
]
