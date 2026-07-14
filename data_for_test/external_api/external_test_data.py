ext_api_valid_data = [
    {
        'operation': {
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
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        'expected_value': 639200.57
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": "90582.51",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'expected_value': 8032462.14
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": "90582.51",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'expected_value': 90582.51
    },

]

ext_api_invalid_data = [

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": 90582.51,
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Сумма должна быть типа str.'
                  'Передан тип float.',
        'expected_value': 'Сумма должна быть типа str.'
                          'Передан тип float.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": 90582,
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Сумма должна быть типа str.'
                  'Передан тип int.',
        'expected_value': 'Сумма должна быть типа str.'
                          'Передан тип int.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": False,
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Сумма должна быть типа str.'
                  'Передан тип bool.',
        'expected_value': 'Сумма должна быть типа str.'
                          'Передан тип bool.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": {1, 2, 3},
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Сумма должна быть типа str.'
                  'Передан тип set.',
        'expected_value': 'Сумма должна быть типа str.'
                          'Передан тип set.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": {'value': 90582.12},
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Сумма должна быть типа str.'
                  'Передан тип dict.',
        'expected_value': 'Сумма должна быть типа str.'
                          'Передан тип dict.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": (90582.12, 4127138.00),
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Сумма должна быть типа str.'
                  'Передан тип tuple.',
        'expected_value': 'Сумма должна быть типа str.'
                          'Передан тип tuple.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": [90582.12, 4127138.00],
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Сумма должна быть типа str.'
                  'Передан тип list.',
        'expected_value': 'Сумма должна быть типа str.'
                          'Передан тип list.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": '90582.51',
                "currency": {
                    "name": "RUB",
                    "code": 51
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Валюта должна быть типа str.'
                  'Передан тип int.',
        'expected_value': 'Валюта должна быть типа str.'
                          'Передан тип int.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": '90582.51',
                "currency": {
                    "name": "RUB",
                    "code": 51.1
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Валюта должна быть типа str.'
                  'Передан тип float.',
        'expected_value': 'Валюта должна быть типа str.'
                          'Передан тип float.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": '90582.51',
                "currency": {
                    "name": "RUB",
                    "code": False
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Валюта должна быть типа str.'
                  'Передан тип bool.',
        'expected_value': 'Валюта должна быть типа str.'
                          'Передан тип bool.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": '90582.51',
                "currency": {
                    "name": "RUB",
                    "code": [1, 2, 3]
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Валюта должна быть типа str.'
                  'Передан тип list.',
        'expected_value': 'Валюта должна быть типа str.'
                          'Передан тип list.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": '90582.51',
                "currency": {
                    "name": "RUB",
                    "code": {'value': 1.1}
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Валюта должна быть типа str.'
                  'Передан тип dict.',
        'expected_value': 'Валюта должна быть типа str.'
                          'Передан тип dict.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": '90582.51',
                "currency": {
                    "name": "RUB",
                    "code": (5, 1, 1)
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Валюта должна быть типа str.'
                  'Передан тип tuple.',
        'expected_value': 'Валюта должна быть типа str.'
                          'Передан тип tuple.'
    },

    {
        'operation': {
            "id": 542678139,
            "state": "EXECUTED",
            "date": "2018-10-14T22:27:25.205631",
            "operationAmount": {
                "amount": '90582.51',
                "currency": {
                    "name": "RUB",
                    "code": {5, 1, 1}
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 2256483756542539",
            "to": "Счет 78808375133947439319"
        },
        'result': 'Валюта должна быть типа str.'
                  'Передан тип set.',
        'expected_value': 'Валюта должна быть типа str.'
                          'Передан тип set.'
    },
]

structure_test_data = [
    {
        'operation': 'test',
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: dict.'
                          f'Передан тип: str.'
    },

    {
        'operation': 9,
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: dict.'
                          f'Передан тип: int.'
    },

    {
        'operation': 9.8,
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: dict.'
                          f'Передан тип: float.'
    },

    {
        'operation': [1, 2, 3],
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: dict.'
                          f'Передан тип: list.'
    },

    {
        'operation': (1, 2, 3),
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: dict.'
                          f'Передан тип: tuple.'
    },

    {
        'operation': {1, 2, 3},
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: dict.'
                          f'Передан тип: set.'
    },

    {
        'operation': {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        'exception_type': KeyError,
        'expected_value': 'Ключ "code" отсутствует в наборе данных.'
    },

    {
        'operation': {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        'exception_type': KeyError,
        'expected_value': 'Ключ "amount" отсутствует в наборе данных.'
    },
]
