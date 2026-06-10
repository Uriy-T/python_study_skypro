def filter_by_state(data_for_filter: list[dict], state: str = 'EXECUTED') -> list[dict] | str:


    available_states = ['EXECUTED', 'CANCELED']

    if not isinstance(data_for_filter, list):
        raise TypeError(f'data_for_filter должен быть list, получен тип: {type(data_for_filter).__name__}')

    if not all(isinstance(item, dict) for item in data_for_filter):
        raise TypeError(f'Все элементы data_for_filter должен быть dict')

    if not isinstance(state, str):
        raise TypeError(f'state должен быть str, получен тип: {type(state).__name__}')

    if state not in available_states:
        raise ValueError(f'Значения state нет в списке доступных состояний. Доступны: {available_states}')

    return [item for item in data_for_filter if item['state'] == state]

