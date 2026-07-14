search_test_valid_data = [
    {
        'transaction_data': [{
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
            "description": "Пополнение счета",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },

            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            },

            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "EUR",
                        "code": "EUR"
                    }
                },
                "description": "Начисление по дивидендам",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            }
        ],
        'search_string': 'Списание по кредиту',
        'expected_result': [
            {
                'id': 41428829,
                'state': 'EXECUTED',
                'date': '2019-07-03T18:35:29.512364',
                'operationAmount': {
                    'amount': '8221.37',
                    'currency': {
                        'name': 'USD',
                        'code': 'USD'
                    }
                },
                'description': 'Списание по кредиту',
                'from': 'MasterCard 7158300734726758',
                'to': 'Счет 35383033474447895560'
            }
        ]
    },

    {
        'transaction_data': [{
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
            "description": "Пополнение счета",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },

            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            },

            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "EUR",
                        "code": "EUR"
                    }
                },
                "description": "Начисление по дивидендам",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            }
        ],
        'search_string': 'по',
        'expected_result': [{
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
            "description": "Пополнение счета",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },

            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            },

            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "EUR",
                        "code": "EUR"
                    }
                },
                "description": "Начисление по дивидендам",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            }

        ]
    }
]

search_test_invalid_data = [
    {
        'transaction_data': 1,
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: int'
    },

    {
        'transaction_data': 1.2,
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: float'
    },

    {
        'transaction_data': False,
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: bool'
    },

    {
        'transaction_data': {'first': 12},
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: dict'
    },

    {
        'transaction_data': (1, 2, 3),
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: tuple'
    },

    {
        'transaction_data': {1, 2, 3},
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: set'
    },

    {
        'transaction_data': [1, 2, 3],
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': ['1', 'Привет'],
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [1.76, 2.1, 63.1],
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [True, False],
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [
            [1, 2, 3],
            [4, 5, 6]
        ],
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [
            {'dict': 1},
            {'dict': 2},
            ['1']
        ],
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [
            (1, 2, 3),
            (4, 5, 6)
        ],
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [
            {1, 2, 3},
            {4, 5, 6}
        ],
        'search_string': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
        ],
        'search_string': 1,
        'exception_type': TypeError,
        'system_answer': 'search_str ожидает тип: str'
                         'Передан тип: int'
    },

    {
        'transaction_data': [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
        ],
        'search_string': 1.79,
        'exception_type': TypeError,
        'system_answer': 'search_str ожидает тип: str'
                         'Передан тип: float'
    },

    {
        'transaction_data': [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
        ],
        'search_string': True,
        'exception_type': TypeError,
        'system_answer': 'search_str ожидает тип: str'
                         'Передан тип: bool'
    },

    {
        'transaction_data': [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
        ],
        'search_string': [1, 2, 3],
        'exception_type': TypeError,
        'system_answer': 'search_str ожидает тип: str'
                         'Передан тип: list'
    },

    {
        'transaction_data': [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
        ],
        'search_string': {'for_search': 'test'},
        'exception_type': TypeError,
        'system_answer': 'search_str ожидает тип: str'
                         'Передан тип: dict'
    },

    {
        'transaction_data': [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
        ],
        'search_string': (1, 2, 3),
        'exception_type': TypeError,
        'system_answer': 'search_str ожидает тип: str'
                         'Передан тип: tuple'
    },

    {
        'transaction_data': [
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Списание по кредиту",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560"
            }
        ],
        'search_string': {1, 2, 3},
        'exception_type': TypeError,
        'system_answer': 'search_str ожидает тип: str'
                         'Передан тип: set'
    },
]
