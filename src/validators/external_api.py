from typing import Any


def data_type_validator(data: dict[str, Any], expected_type: type) -> None:
    actual_type = type(data)
    if actual_type != expected_type:
        raise TypeError(
            f"Ожидаемый тип данных: {expected_type.__name__}."
            f"Передан тип: {actual_type.__name__}."
        )


def structure_validator(
    data_for_scan: dict[str, Any], search_element: str
) -> None:
    if search_element not in data_for_scan:
        raise KeyError(f'Ключ "{search_element}" отсутствует в наборе данных.')
