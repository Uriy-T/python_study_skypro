def filter_by_state(data_for_filter: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция-фильтр, отделяющая объекты с данными из общего набора в соответствии со значением параметра state.
    :param data_for_filter: список объектов (словарей), на основе которых проводится фильтрация.
    :param state: тип состояния, по которому проводится фильтрация объектов из параметра data_for_filter.
    В базовой версии доступны состояния 'EXECUTED' и 'CANCELED'. Значение параметра по умолчанию: 'EXECUTED'.

    :return:
    - При подаче на вход валидных данных, возвращает список объектов (словарей),
    обладающих указанным значением ключа state.
    - При подаче на вход невалидных данных возвращает исключения соответствующие варианту неверного ввода.
    """

    available_states = ["EXECUTED", "CANCELED"]

    if not isinstance(data_for_filter, list):
        raise TypeError(f"data_for_filter должен быть list, получен тип: {type(data_for_filter).__name__}")

    if not all(isinstance(item, dict) for item in data_for_filter):
        raise TypeError("Все элементы data_for_filter должен быть dict")

    if not isinstance(state, str):
        raise TypeError(f"state должен быть str, получен тип: {type(state).__name__}")

    if state not in available_states:
        raise ValueError(f"Значения state нет в списке доступных состояний. Доступны: {available_states}")

    for i, item in enumerate(data_for_filter):
        if "state" not in item:
            raise KeyError(f"Элемент с индексом {i} не содержит ключ 'state'")

    return [item for item in data_for_filter if item["state"] == state]


def sort_by_date(data_for_sort: list[dict], sort_order_reverse: bool = True) -> list[dict]:
    """
    Функция сортирует полученный набор объектов (словарей) по значению параметра date.
    :param data_for_sort: список объектов (словарей), которые нужно отсортировать
    :param sort_order_reverse: параметр управления направлением сортировки по убыванию/возрастанию.
    По умолчанию сортировка происходит по убыванию (True)

    :return:
    - При подаче на вход валидных данных, возвращает список объектов (словарей) отсортированный по дате (date),
    в заданном направлении.
    - При подаче на вход невалидных данных возвращает исключения соответствующие варианту неверного ввода.
    """

    if not isinstance(data_for_sort, list):
        raise TypeError(f"data_for_sort должен быть list, получен тип: {type(data_for_sort).__name__}")

    if not all(isinstance(item, dict) for item in data_for_sort):
        raise TypeError("Все элементы data_for_filter должен быть dict")

    if not isinstance(sort_order_reverse, bool):
        raise TypeError(f"state должен быть str, получен тип: {type(sort_order_reverse).__name__}")

    for i, item in enumerate(data_for_sort):
        if "date" not in item:
            raise KeyError(f"Элемент с индексом {i} не содержит ключ 'date'")

    return sorted(data_for_sort, key=lambda x: x["date"], reverse=sort_order_reverse)
