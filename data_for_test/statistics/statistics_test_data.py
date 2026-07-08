statistics_test_valid_data = [
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
            "description": "Списание по кредиту",
            "from": "Maelisto 1596837868705199",
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
                "description": "Пополнение счета",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            }
        ],
        'count_categories': ['Списание по кредиту'],
        'expected_result': {'Списание по кредиту': 2}
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
            "description": "Списание по кредиту",
            "from": "Maelisto 1596837868705199",
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
                "description": "Пополнение счета",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            }
        ],
        'count_categories': ['Списание по кредиту', 'Пополнение счета'],
        'expected_result': {'Списание по кредиту': 2, 'Пополнение счета': 1}
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
            "from": "Maelisto 1596837868705199",
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
                "description": "Списание по кредиту",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            }
        ],
        'count_categories': ['Списание по кредиту', 'Пополнение счета', 'Выплаты по дивидендам'],
        'expected_result': {'Списание по кредиту': 2, 'Пополнение счета': 1, 'Выплаты по дивидендам': 0}
    }
]

statistics_test_invalid_data = [
    # Проверяются типы данных для коллекции транзакций
    {
        'transaction_data': 1,
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: int'
    },

    {
        'transaction_data': 1.2,
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: float'
    },

    {
        'transaction_data': False,
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: bool'
    },

    {
        'transaction_data': {'first': 12},
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: dict'
    },

    {
        'transaction_data': (1, 2, 3),
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: tuple'
    },

    {
        'transaction_data': {1, 2, 3},
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'transactions ожидает тип: list'
                         'Передан тип: set'
    },
    # Проверяются типы данных для элементов коллекции транзакций
    {
        'transaction_data': [1, 2, 3],
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': ['1', 'Привет'],
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [1.76, 2.1, 63.1],
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [True, False],
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [
            [1, 2, 3],
            [4, 5, 6]
        ],
        'count_categories': 'Начисление',
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
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [
            (1, 2, 3),
            (4, 5, 6)
        ],
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },

    {
        'transaction_data': [
            {1, 2, 3},
            {4, 5, 6}
        ],
        'count_categories': 'Начисление',
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка transactions'
                         'являются dict'
    },
    # Проверяются типы данных для списка категорий
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
        'count_categories': 1,
        'exception_type': TypeError,
        'system_answer': 'categories ожидает тип: list'
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
        'count_categories': 1.79,
        'exception_type': TypeError,
        'system_answer': 'categories ожидает тип: list'
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
        'count_categories': True,
        'exception_type': TypeError,
        'system_answer': 'categories ожидает тип: list'
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
        'count_categories': {'for_search': 'test'},
        'exception_type': TypeError,
        'system_answer': 'categories ожидает тип: list'
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
        'count_categories': (1, 2, 3),
        'exception_type': TypeError,
        'system_answer': 'categories ожидает тип: list'
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
        'count_categories': {1, 2, 3},
        'exception_type': TypeError,
        'system_answer': 'categories ожидает тип: list'
                         'Передан тип: set'
    },
    # Проверяютсятся типы данных для элементов списка категорий
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
        'count_categories': [1, 2, 3],
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка categories'
                         'являются str'
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
        'count_categories': ['1', '2', 3.2],
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка categories'
                         'являются str'
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
        'count_categories': ['1', '2', 3],
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка categories'
                         'являются str'
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
        'count_categories': ['1', '2', 3.2],
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка categories'
                         'являются str'
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
        'count_categories': ['1', '2', False],
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка categories'
                         'являются str'
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
        'count_categories': ['1', '2', [3, 3]],
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка categories'
                         'являются str'
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
        'count_categories': ['1', '2', {'category': 3}],
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка categories'
                         'являются str'
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
        'count_categories': ['1', '2', (3, 4, 5)],
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка categories'
                         'являются str'
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
        'count_categories': ['1', '2', {3, 4, 5}],
        'exception_type': TypeError,
        'system_answer': 'Не все элементы списка categories'
                         'являются str'
    },
]
