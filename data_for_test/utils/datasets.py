get_info_valid_data = [{
    'file_for_read': './data_for_test/utils/valid_operations.json',
    'expected_data': [
        {
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
            "description": "Перевод организации",
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
            "description": "Перевод организации",
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
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    ]
}]

get_info_invalid_data = [
    {'file_for_read': './data_for_test/utils/not_exist_operations.json',
     'expected_data': []},
    {'file_for_read': './data_for_test/utils/invalid_operations_empty.json',
     'expected_data': []},
    {'file_for_read': './data_for_test/utils/invalid_operations_not_list.json',
     'expected_data': []},
]

get_info_path_invalid_data = [
    {
        'path': 9,
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: str.'
                          f'Передан тип: int.'
    },

    {
        'path': 9.12,
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: str.'
                          f'Передан тип: float.'
    },

    {
        'path': True,
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: str.'
                          f'Передан тип: bool.'
    },

    {
        'path': [1, 2, 3],
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: str.'
                          f'Передан тип: list.'
    },

    {
        'path': (1, 2, 3),
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: str.'
                          f'Передан тип: tuple.'
    },

    {
        'path': {1, 2, 3},
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: str.'
                          f'Передан тип: set.'
    },

{
        'path': {'path': 'test_invalid_path'},
        'exception_type': TypeError,
        'expected_value': f'Ожидаемый тип данных: str.'
                          f'Передан тип: dict.'
    },
]
