
get_info_valid_data = [
    {
        'file_for_read': './data_for_test/table_data_readers/valid_transactions.xlsx',
        'expected_data': [
            {
                'id': 650703,
                'state': 'EXECUTED',
                'date': '2023-09-05T11:30:32Z',
                'amount': 16210,
                'currency_name': 'Sol',
                'currency_code': 'PEN',
                'from': 'Счет 58803664561298323391',
                'to': 'Счет 39745660563456619397',
                'description': 'Перевод организации'
            },

            {
                'id': 3598919,
                'state': 'EXECUTED',
                'date': '2020-12-06T23:00:58Z',
                'amount': 29740,
                'currency_name': 'Peso',
                'currency_code': 'COP',
                'from': 'Discover 3172601889670065',
                'to': 'Discover 0720428384694643',
                'description': 'Перевод с карты на карту'
            },

            {
                'id': 593027,
                'state': 'CANCELED',
                'date': '2023-07-22T05:02:01Z',
                'amount': 30368,
                'currency_name': 'Shilling',
                'currency_code': 'TZS',
                'from': 'Visa 1959232722494097',
                'to': 'Visa 6804119550473710',
                'description': 'Перевод с карты на карту'
            }
        ]
    }]

get_info_invalid_data = [
    {
        'file_for_read': './data_for_test/table_data_readers/no_exist_transactions_file.xlsx',
        'expected_data': []
    },

    {
        'file_for_read': './data_for_test/table_data_readers/transactions_excel_empty_table.xlsx',
        'expected_data': []
    },

    {
        'file_for_read': './data_for_test/table_data_readers/transactions_excel_full_empty.xlsx',
        'expected_data': []
    },
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
