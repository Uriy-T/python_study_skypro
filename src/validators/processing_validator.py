from datetime import datetime


def dff_validator(data: list[dict]) -> None:
    if not isinstance(data, list):
        raise TypeError(
            f"data_for_filter должен быть list."
            f"Получен тип: {type(data).__name__}"
        )

    if not data or data == [{}]:
        raise ValueError("Данные для обработки не предоставлены.")

    if not all(isinstance(item, dict) for item in data):
        raise TypeError("Все элементы data_for_filter должны быть dict")

    for _, item in enumerate(data):
        if "id" not in item:
            raise KeyError(
                "В одном или более элементах data_for_filter"
                "отсутствует ключ: id"
            )

    for _, item in enumerate(data):
        if "state" not in item:
            raise KeyError(
                "В одном или более элементах data_for_filter"
                "отсутствует ключ: state"
            )

    for _, item in enumerate(data):
        if "date" not in item:
            raise KeyError(
                "В одном или более элементах data_for_filter"
                "отсутствует ключ: date"
            )

    if not all(type(item["id"]) is int for item in data):
        raise TypeError(
            "В одном или более элементах data_for_filter,"
            "значение ключа id не является int"
        )

    if not all(isinstance(item["state"], str) for item in data):
        raise TypeError(
            "В одном или более элементах data_for_filter,"
            "значение ключа state не является str"
        )

    if not all(isinstance(item["date"], str) for item in data):
        raise TypeError(
            "В одном или более элементах data_for_filter,"
            "значение ключа date не является str"
        )

    for _, item in enumerate(data):
        try:
            datetime.fromisoformat(item["date"])
        except ValueError:
            raise ValueError(
                "В одном или более элементах data_for_filter,"
                "значение ключа date не является форматом ISO"
            )


available_states = ['EXECUTED', 'CANCELED', 'PENDING']


def state_validator(state: str) -> None:
    if not isinstance(state, str):
        raise TypeError(
            f"state должен быть str." f"Получен тип: {type(state).__name__}"
        )

    if state not in available_states:
        raise ValueError(
            f"Значения state нет в списке доступных состояний."
            f"Доступны: {available_states}"
        )


def dfs_validator(data_for_sort: list[dict]) -> None:
    if not isinstance(data_for_sort, list):
        raise TypeError(
            f"data_for_sort должен быть list."
            f"Получен тип: {type(data_for_sort).__name__}"
        )

    if not data_for_sort or data_for_sort == [{}]:
        raise ValueError("Данные для сортировки не предоставлены.")

    if not all(isinstance(item, dict) for item in data_for_sort):
        raise TypeError("Все элементы data_for_sort должны быть dict")

    for _, item in enumerate(data_for_sort):
        if "id" not in item:
            raise KeyError(
                "В одном или более элементах data_for_sort "
                "отсутствует ключ: id"
            )

    for _, item in enumerate(data_for_sort):
        if "state" not in item:
            raise KeyError(
                "В одном или более элементах data_for_sort "
                "отсутствует ключ: state"
            )

    for _, item in enumerate(data_for_sort):
        if "date" not in item:
            raise KeyError(
                "В одном или более элементах data_for_sort "
                "отсутствует ключ: date"
            )

    if not all(type(item["id"]) is int for item in data_for_sort):
        raise TypeError(
            "В одном или более элементах data_for_sort,"
            "значение ключа id не является int"
        )

    if not all(isinstance(item["state"], str) for item in data_for_sort):
        raise TypeError(
            "В одном или более элементах data_for_sort,"
            "значение ключа state не является str"
        )

    if not all(isinstance(item["date"], str) for item in data_for_sort):
        raise TypeError(
            "В одном или более элементах data_for_sort,"
            "значение ключа date не является str"
        )

    for _, item in enumerate(data_for_sort):
        try:
            datetime.fromisoformat(item["date"])
        except ValueError:
            raise ValueError(
                "В одном или более элементах data_for_sort,"
                "значение ключа date не является форматом ISO"
            )

    for i, item in enumerate(data_for_sort):
        if "date" not in item:
            raise KeyError(f"Элемент с индексом {i} не содержит ключ 'date'")


def order_validator(sort_order: bool) -> None:
    if not isinstance(sort_order, bool):
        raise TypeError(
            f"state должен быть str."
            f"Получен тип: {type(sort_order).__name__}"
        )
