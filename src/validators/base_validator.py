from typing import Any


def data_type_validator(
        input_data: Any,
        expected_type: type,
        param_name: str) -> None:
    actual_type = type(input_data)
    if actual_type != expected_type:
        raise TypeError(f'{param_name} ожидает тип: {expected_type.__name__}'
                        f'Передан тип: {actual_type.__name__}'
                        )


def collection_elements_type_validator(
        input_data: Any,
        expected_type: type,
        param_name: str
) -> None:
    if not all(isinstance(elem, expected_type) for elem in input_data):
        raise TypeError(f'Не все элементы списка {param_name}'
                        f'являются {expected_type.__name__}')
