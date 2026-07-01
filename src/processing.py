from src.validators.processing_validator import (
    dff_validator,
    dfs_validator,
    order_validator,
    state_validator,
)


def filter_by_state(
    data_for_filter: list[dict], state: str = "EXECUTED"
) -> list[dict]:
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

    dff_validator(data_for_filter)
    state_validator(state)

    return [item for item in data_for_filter if item["state"] == state]


def sort_by_date(
    data_for_sort: list[dict], sort_order: bool = True
) -> list[dict]:
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

    dfs_validator(data_for_sort)
    order_validator(sort_order)

    return sorted(data_for_sort, key=lambda x: x["date"], reverse=sort_order)
