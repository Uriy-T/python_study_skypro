sdb_valid_data = [
    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],

        'sort_order': True,

        'sorted_list': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],

        'sort_order': False,

        'sorted_list': [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    },

]

sdb_valid_data_partial = [
    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                          {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                          {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}],

        'sorted_list': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    }
]

sdb_invalid_data = [

    {
        'data_for_sort': [],
        'sort_order': True,
        'system_answer': 'Данные для сортировки не предоставлены.',
        'exception_type': ValueError
    },

    {
        'data_for_sort': [{}],
        'sort_order': True,
        'system_answer': 'Данные для сортировки не предоставлены.',
        'exception_type': ValueError
    },

    {
        'data_for_sort': {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        'sort_order': True,
        'system_answer': 'data_for_sort должен быть list.'
                         'Получен тип: dict',
        'exception_type': TypeError
    },

    {
        'data_for_sort': ({'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},),
        'sort_order': True,
        'system_answer': 'data_for_sort должен быть list.'
                         'Получен тип: tuple',
        'exception_type': TypeError
    },

    {
        'data_for_sort': {41428829, 594226727},
        'sort_order': True,
        'system_answer': 'data_for_sort должен быть list.'
                         'Получен тип: set',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          [594226727, 'CANCELED', '2018-09-12T21:27:25.241689']],
        'sort_order': True,
        'system_answer': 'Все элементы data_for_sort должны быть dict',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          {594226727, 'CANCELED', '2018-09-12T21:27:25.241689'}],
        'sort_order': True,
        'system_answer': 'Все элементы data_for_sort должны быть dict',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                          (594226727, 'CANCELED', '2018-09-12T21:27:25.241689')],
        'sort_order': True,
        'system_answer': 'Все элементы data_for_sort должны быть dict',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': "В одном или более элементах data_for_sort "
                         "отсутствует ключ: id",
        'exception_type': KeyError
    },

    {
        'data_for_sort': [{'id': 41428829, 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': "В одном или более элементах data_for_sort "
                         "отсутствует ключ: state",
        'exception_type': KeyError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED'}],
        'sort_order': True,
        'system_answer': "В одном или более элементах data_for_sort "
                         "отсутствует ключ: date",
        'exception_type': KeyError
    },

    {
        'data_for_sort': [{'id': '41428829', 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа id не является int',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 4142882.9, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа id не является int',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': [1, 2, 3], 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа id не является int',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': {'prefix': 'invest', 'number_id': 18762246}, 'state': 'EXECUTED',
                           'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа id не является int',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': {'invest', 18762246}, 'state': 'EXECUTED',
                           'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа id не является int',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': (1, 2, 3), 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа id не является int',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': None, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа id не является int',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': True, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа id не является int',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 1, 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа state не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 1.14, 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа state не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': False, 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа state не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': None, 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа state не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': ['pre', 'execute'], 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа state не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [
            {'id': 41428829, 'state': {'additional': 'pre', 'base': 'execute'}, 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа state не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': {'pre', 'execute'}, 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа state не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': ('pre', 'execute'), 'date': '2019-07-03T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа state не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': '3T18:35:29.512364'}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа date не является форматом ISO',
        'exception_type': ValueError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': 54}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа date не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': 76.1}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа date не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': True}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа date не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': None}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа date не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': [12, 7, 2023]}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа date не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': (12, 7, 2023)}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа date не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': {12, 7, 2023}}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа date не является str',
        'exception_type': TypeError
    },

    {
        'data_for_sort': [{'id': 41428829, 'state': 'EXECUTED', 'date': {'day': 12, 'month': 7, 'year': 2023}}],
        'sort_order': True,
        'system_answer': 'В одном или более элементах data_for_sort,'
                         'значение ключа date не является str',
        'exception_type': TypeError
    },

]
