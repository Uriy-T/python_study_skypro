card_valid_data = [
    {
        'card_number': 1234567890123456,
        'masked_value': '1234 56** **** 3456'
    }
]

card_invalid_data = [
    {
        'card_number': 123456789012345,
        'system_answer':
            'Номер карты должен содержать 16 цифр',
        'exception_type': ValueError
    },

    {
        'card_number': 12345678901234567,
        'system_answer':
            'Номер карты должен содержать 16 цифр',
        'exception_type': ValueError
    },

    {
        'card_number': '1234567890123456',
        'system_answer':
            'Переданное значение не является int',
        'exception_type': TypeError
    },

    {
        'card_number': 123456789012345.6,
        'system_answer':
            'Переданное значение не является int',
        'exception_type': TypeError
    },

    {
        'card_number': False,
        'system_answer':
            'Переданное значение не является int',
        'exception_type': TypeError
    },

    {
        'card_number': -1234567890123456,
        'system_answer':
            'Переданное число не является положительным',
        'exception_type': ValueError
    },

    {
        'card_number': None,
        'system_answer':
            'Переданное значение не является int',
        'exception_type': TypeError
    }
]

account_valid_data = [
    {'account': 98765432109876543210,
     'masked_value': '****3210'}
]

account_invalid_data = [
    {
        'account': 1234567890123456789,  # 19 цифр
        'system_answer':
            'Номер счета должен содержать 20 цифр',
        'exception_type': ValueError
    },

    {
        'account': 123456789012345678901,  # 21 цифра
        'system_answer':
            'Номер счета должен содержать 20 цифр',
        'exception_type': ValueError
    },

    {
        'account': '12345678901234567890',
        'system_answer':
            'Переданное значение не является int',
        'exception_type': TypeError
    },

    {
        'account': 12345678901234567890.0,
        'system_answer':
            'Переданное значение не является int',
        'exception_type': TypeError
    },

    {
        'account': True,
        'system_answer':
            'Переданное значение не является int',
        'exception_type': TypeError
    },

    {
        'account': -98765432109876543210,
        'system_answer':
            'Номер счета не может быть отрицательным',
        'exception_type': ValueError
    },

    # {
    #     'account': 0,
    #     'system_answer':
    #         'Номер счета не может быть нулевым',
    #     'exception_type': ValueError
    # },

    {
        'account': None,
        'system_answer':
            'Переданное значение не является int',
        'exception_type': TypeError
    }
]
