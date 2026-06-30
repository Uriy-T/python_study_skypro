def path_type_validator(data: str, expected_type: type) -> None:
    actual_type = type(data)
    if actual_type != expected_type:
        raise TypeError(
            f"Ожидаемый тип данных: {expected_type.__name__}."
            f"Передан тип: {actual_type.__name__}."
        )
