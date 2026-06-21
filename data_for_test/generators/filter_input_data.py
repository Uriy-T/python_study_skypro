from typing import Any

available_currencies = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD",
    "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "GBP", "GEL", "GHS", "GIP",
    "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF", "IDR",
    "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES", "KGS",
    "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP", "LKR",
    "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK", "MNT", "MOP",
    "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD", "NGN", "NIO",
    "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP", "PKR", "PLN",
    "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD", "SCR", "SDG",
    "SEK", "SGD", "SHP", "SLL", "SOS", "SRD", "SSP", "STN", "SVC", "SYP",
    "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TWD", "TZS",
    "UAH", "UGX", "USD", "UYU", "UZS", "VED", "VES", "VND", "VUV", "WST",
    "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL",
]

trans_valid_data: list[dict[str, Any]] = [
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
        }],
        'currency': 'USD',
        'expected_seq': [
            {
                'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                'to': 'Счет 11776614605963066702'
            },
            {
                'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                'to': 'Счет 75651667383060284188'
            }]
    },

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
        }],
        'currency': 'EUR',
        'expected_seq': [
            {
                'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689',
                'operationAmount': {'amount': '5412.50', 'currency': {'name': 'EUR', 'code': 'EUR'}},
                'description': 'Перевод с карты на счет', 'from': 'Visa 1234567890123456',
                'to': 'Счет 11776614605963066702'
            }
        ]
    },

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
        }],
        'currency': 'RUB',
        'expected_seq': [
            {
                'id': 873460982, 'state': 'EXECUTED', 'date': '2020-01-15T14:30:12.456789',
                'operationAmount': {'amount': '15789.00', 'currency': {'name': 'RUB', 'code': 'RUB'}},
                'description': 'Перевод на карту', 'from': 'Счет 12345678901234567890', 'to': 'Visa 9876543210987654'
            }
        ]
    }

]

trans_invalid_data: list[dict[str, Any]] = [

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
        'currency': 'USD',
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
        'currency': 'USD',
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
        'currency': 'USD',
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
        'currency': 'USD',
        'system_answer': 'В одном или более элементах списка данных нет ключа "description"',
        'exception_type': KeyError
    },

    {
        'transaction': 'Transaction',
        'currency': 'USD',
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: str",
        'exception_type': TypeError
    },

    {
        'transaction': 9,
        'currency': 'USD',
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: int",
        'exception_type': TypeError
    },

    {
        'transaction': 9.152,
        'currency': 'USD',
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: float",
        'exception_type': TypeError
    },

    {
        'transaction': True,
        'currency': 'USD',
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: bool",
        'exception_type': TypeError
    },

    {
        'transaction': None,
        'currency': 'USD',
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

        'currency': 'USD',
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: dict",
        'exception_type': TypeError
    },

    {
        'transaction':
            ("id", "939719570"),

        'currency': 'USD',
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: tuple",
        'exception_type': TypeError
    },

    {
        'transaction':
            {"id", "939719570"},

        'currency': 'USD',
        'system_answer': f"Данные должны быть типом list."
                         f"Предоставлен тип: set",
        'exception_type': TypeError
    },

    {
        'transaction': [{}],
        'currency': 'USD',
        'system_answer': 'Данные не предоставлены',
        'exception_type': ValueError
    },

    {
        'transaction': [],
        'currency': 'USD',
        'system_answer': 'Данные не предоставлены',
        'exception_type': ValueError
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
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'currency': 'DBA',
        'system_answer': 'Введено название не существующей валюты',
        'exception_type': ValueError
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
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'currency': 1,
        'system_answer': f"Значение currency должно быть типом str."
                         f"Предоставлен тип: int",
        'exception_type': TypeError
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
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'currency': 56.37,
        'system_answer': f"Значение currency должно быть типом str."
                         f"Предоставлен тип: float",
        'exception_type': TypeError
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
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'currency': False,
        'system_answer': f"Значение currency должно быть типом str."
                         f"Предоставлен тип: bool",
        'exception_type': TypeError
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
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'currency': ['USD', 'RUB'],
        'system_answer': f"Значение currency должно быть типом str."
                         f"Предоставлен тип: list",
        'exception_type': TypeError
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
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'currency': ('USD', 'RUB'),
        'system_answer': f"Значение currency должно быть типом str."
                         f"Предоставлен тип: tuple",
        'exception_type': TypeError
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
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'currency': ('USD', 'RUB'),
        'system_answer': f"Значение currency должно быть типом str."
                         f"Предоставлен тип: tuple",
        'exception_type': TypeError
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
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'currency': {'USD', 'RUB'},
        'system_answer': f"Значение currency должно быть типом str."
                         f"Предоставлен тип: set",
        'exception_type': TypeError
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
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
        ],
        'currency': {'United States': 'USD', 'Russia': 'RUB'},
        'system_answer': f"Значение currency должно быть типом str."
                         f"Предоставлен тип: dict",
        'exception_type': TypeError
    },
]
