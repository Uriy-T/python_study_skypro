from datetime import datetime


def filter_by_state(data_for_filter: list[dict],
                    state: str = "EXECUTED") -> list[dict]:
    """
    Функция отделяет объекты с данными из общего набора по значению rest.
    :param data_for_filter: список словарей, для фильтрации.
    :param state: тип состояния, по которому проводится фильтрация.

    :return:
    - При подаче на вход валидных данных, возвращает список словарей,
    обладающих указанным значением ключа state.
    - При подаче на вход невалидных данных возвращает исключения,
    соответствующие случаю неверного ввода.
    """

    available_states = ["EXECUTED", "CANCELED"]

    if not isinstance(data_for_filter, list):
        raise TypeError(f"data_for_filter должен быть list."
                        f"Получен тип: {type(data_for_filter).__name__}")

    if not data_for_filter or data_for_filter == [{}]:
        raise ValueError('Данные для фильтрации не предоставлены.')

    if not all(isinstance(item, dict) for item in data_for_filter):
        raise TypeError("Все элементы data_for_filter должны быть dict")

    for _, item in enumerate(data_for_filter):
        if "id" not in item:
            raise KeyError("В одном или более элементах data_for_filter"
                           "отсутствует ключ: id")

    for _, item in enumerate(data_for_filter):
        if "state" not in item:
            raise KeyError("В одном или более элементах data_for_filter"
                           "отсутствует ключ: state")

    for _, item in enumerate(data_for_filter):
        if "date" not in item:
            raise KeyError("В одном или более элементах data_for_filter"
                           "отсутствует ключ: date")

    if not all(type(item['id']) is int for item in data_for_filter):
        raise TypeError("В одном или более элементах data_for_filter,"
                        "значение ключа id не является int")

    if not all(isinstance(item['state'], str) for item in data_for_filter):
        raise TypeError("В одном или более элементах data_for_filter,"
                        "значение ключа state не является str")

    if not all(isinstance(item['date'], str) for item in data_for_filter):
        raise TypeError("В одном или более элементах data_for_filter,"
                        "значение ключа date не является str")

    for _, item in enumerate(data_for_filter):
        try:
            datetime.fromisoformat(item['date'])
        except:
            raise ValueError("В одном или более элементах data_for_filter,"
                             "значение ключа date не является форматом ISO")

    if not isinstance(state, str):
        raise TypeError(f"state должен быть str."
                        f"Получен тип: {type(state).__name__}")

    if state not in available_states:
        raise ValueError(f"Значения state нет в списке доступных состояний."
                         f"Доступны: {available_states}")

    return [item for item in data_for_filter if item["state"] == state]


def sort_by_date(data_for_sort: list[dict],
                 sort_order: bool = True) -> list[dict]:
    """
    Функция сортирует полученный набор словарей по значению параметра date.
    :param data_for_sort: список словарей для сортировки.
    :param sort_order: контролирует направление сортировки.
    По умолчанию сортировка происходит по убыванию (True)

    :return:
    - При вводе валидных данных, возвращает отсортированный список словарей,
    в заданном направлении.
    - При вводе невалидных данных возвращает исключения,
    соответствующие случаю неверного ввода.
    """

    if not isinstance(data_for_sort, list):
        raise TypeError(f"data_for_sort должен быть list."
                        f"Получен тип: {type(data_for_sort).__name__}")

    if not data_for_sort or data_for_sort == [{}]:
        raise ValueError('Данные для сортировки не предоставлены.')

    if not all(isinstance(item, dict) for item in data_for_sort):
        raise TypeError("Все элементы data_for_sort должны быть dict")

    for _, item in enumerate(data_for_sort):
        if "id" not in item:
            raise KeyError("В одном или более элементах data_for_sort "
                           "отсутствует ключ: id")

    for _, item in enumerate(data_for_sort):
        if "state" not in item:
            raise KeyError("В одном или более элементах data_for_sort "
                           "отсутствует ключ: state")

    for _, item in enumerate(data_for_sort):
        if "date" not in item:
            raise KeyError("В одном или более элементах data_for_sort "
                           "отсутствует ключ: date")

    if not all(type(item['id']) is int for item in data_for_sort):
        raise TypeError("В одном или более элементах data_for_sort,"
                        "значение ключа id не является int")

    if not all(isinstance(item['state'], str) for item in data_for_sort):
        raise TypeError("В одном или более элементах data_for_sort,"
                        "значение ключа state не является str")

    if not all(isinstance(item['date'], str) for item in data_for_sort):
        raise TypeError("В одном или более элементах data_for_sort,"
                        "значение ключа date не является str")

    for _, item in enumerate(data_for_sort):
        try:
            datetime.fromisoformat(item['date'])
        except:
            raise ValueError("В одном или более элементах data_for_sort,"
                             "значение ключа date не является форматом ISO")

    if not isinstance(sort_order, bool):
        raise TypeError(f"state должен быть str."
                        f"Получен тип: {type(sort_order).__name__}")

    for i, item in enumerate(data_for_sort):
        if "date" not in item:
            raise KeyError(f"Элемент с индексом {i} не содержит ключ 'date'")

    return sorted(data_for_sort, key=lambda x: x["date"], reverse=sort_order)
