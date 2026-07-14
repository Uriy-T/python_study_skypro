from typing import Any


def param_packer(data: list[dict[str, Any]]) -> str:
    """
    Анализирует входную структуру данных и формирует список параметров
    для тестирования в pytest.mark.parametrize().
    :param data: входящий список словарей для анализа.
    :return: строка с перечислением параметров для тестирования
    объекта.
    """
    return ", ".join(list(data[0].keys()))


def value_packer(data: list[dict[str, Any]]) -> list[tuple]:
    """
    Анализирует входную структуру данных и формирует список наборов
    значений для тестирования в pytest.mark.parametrize().
    :param data: входящий список словарей для анализа.
    :return: список кортежей содержащих перечисление значений
    для тестирования объекта.
    """
    return [tuple(item.values()) for item in data]
