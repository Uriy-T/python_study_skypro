from config import available_currencies


def data_type_validator(data: list[dict]) -> None:
    if not isinstance(data, list):
        raise TypeError(
            f"Данные должны быть типом list."
            f"Предоставлен тип: {type(data).__name__}"
        )

    if not all(isinstance(item, dict) for item in data):
        raise TypeError(
            "Один или более элементов списка данных не являются dict"
        )


def structure_validator(data: list[dict]) -> None:
    if not data or data == [{}]:
        raise ValueError("Данные не предоставлены")

    if not all("operationAmount" in item for item in data):
        raise KeyError(
            "В одном или более элементах списка данных"
            ' нет ключа "operationAmount"'
        )

    if not all("currency" in item["operationAmount"] for item in data):
        raise KeyError(
            'В одном или более элементах списка данных нет ключа "currency"'
        )

    if not all("name" in item["operationAmount"]["currency"] for item in data):
        raise KeyError(
            'В одном или более элементах списка данных нет ключа "name"'
        )

    if not all("description" in item for item in data):
        raise KeyError(
            'В одном или более элементах списка данных нет ключа "description"'
        )


def currency_validator(currency: str) -> None:
    if not isinstance(currency, str):
        raise TypeError(
            f"Значение currency должно быть типом str."
            f"Предоставлен тип: {type(currency).__name__}"
        )

    if currency not in available_currencies:
        raise ValueError("Введено название не существующей валюты")


def interval_validator(start: int, end: int) -> None:
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError(
            f"Значения и start и end должны быть int."
            f"Предоставлены типы:\n"
            f"start: {type(start).__name__}\n"
            f"end: {type(end).__name__}"
        )
    if type(start) is bool or type(end) is bool:
        raise TypeError(
            f"Значения и start и end должны быть int."
            f"Предоставлены типы:\n"
            f"start: {type(start).__name__}\n"
            f"end: {type(end).__name__}"
        )
