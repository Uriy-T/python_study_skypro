descr_valid_data: list[dict] = [
    {'transaction': [
        {
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
        },

        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },

        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "5412.50",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Visa 1234567890123456",
            "to": "Счет 11776614605963066702"
        },

        {
            "id": 615064591,
            "state": "EXECUTED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {
                "amount": "325.75",
                "currency": {
                    "name": "GBP",
                    "code": "GBP"
                }
            },
            "description": "Оплата услуг",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },

        {
            "id": 873460982,
            "state": "EXECUTED",
            "date": "2020-01-15T14:30:12.456789",
            "operationAmount": {
                "amount": "15789.00",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод на карту",
            "from": "Счет 12345678901234567890",
            "to": "Visa 9876543210987654"
        },

        {
            "id": 234567891,
            "state": "EXECUTED",
            "date": "2021-06-20T10:15:30.123456",
            "operationAmount": {
                "amount": "85000.00",
                "currency": {
                    "name": "CNY",
                    "code": "CNY"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 19708645243227258542",
            "to": "Счет 11776614605963066702"
        }
    ],
        'expected_seq': [
            'Перевод организации',
            'Перевод со счета на счет',
            'Перевод с карты на счет',
            'Оплата услуг',
            'Перевод на карту',
            'Перевод организации'
        ]
    }
]

descr_invalid_data: list[dict] = [

    {
        'transaction': [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },

        ],
        'system_answer': 'В одном или более элементах списка данных нет ключа "operationAmount"',
        'exception_type': KeyError
    },

    {
        'transaction': [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07"
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'system_answer': 'В одном или более элементах списка данных нет ключа "currency"',
        'exception_type': KeyError
    },

    {
        'transaction': [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'system_answer': 'В одном или более элементах списка данных нет ключа "name"',
        'exception_type': KeyError
    },

    {
        'transaction': [
            {
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
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'system_answer': 'В одном или более элементах списка данных нет ключа "description"',
        'exception_type': KeyError
    },

    {
        'transaction': 'Transaction',
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: str",
        'exception_type': TypeError
    },

    {
        'transaction': 9,
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: int",
        'exception_type': TypeError
    },

    {
        'transaction': 9.152,
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: float",
        'exception_type': TypeError
    },

    {
        'transaction': True,
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: bool",
        'exception_type': TypeError
    },

    {
        'transaction': None,
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: NoneType",
        'exception_type': TypeError
    },

    {
        'transaction':
            {
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
            },

        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: dict",
        'exception_type': TypeError
    },

    {
        'transaction':
            ("id", "939719570"),

        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: tuple",
        'exception_type': TypeError
    },

    {
        'transaction':
            {"id", "939719570"},

        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: set",
        'exception_type': TypeError
    },

    {
        'transaction': [{}],
        'system_answer': 'Данные не предоставлены',
        'exception_type': ValueError
    },

    {
        'transaction': [],
        'system_answer': 'Данные не предоставлены',
        'exception_type': ValueError
    }
]
