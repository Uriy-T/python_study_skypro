from typing import Any, Generator

from src.valodators.generators_validators import (currency_validator,
                                                  data_type_validator,
                                                  interval_validator,
                                                  structure_validator)


def filter_by_currency(
    transactions: list[dict], currency: str
) -> Generator[dict[Any, Any], None, None]:
    """
    Функция фильтрует список операций по параметру валюты
    :param transactions: принимает список объектов операций
    :param currency: принимает строку обозначения валюты
    для фильтрации списка операций
    :return: генератор, выдающий отфильтрованные объекты
    операций.
    """
    data_type_validator(transactions)
    structure_validator(transactions)
    currency_validator(currency)
    return (
        operation
        for operation in transactions
        if operation["operationAmount"]["currency"]["name"] == currency
    )


def transaction_descriptions(
    transactions: list[dict],
) -> Generator[dict[Any, Any], None, None]:
    """
    Функция извлекает описание транзакций из каждого
    объекта предоставленного для обработки.
    :param transactions: принимает список объектов операций
    :return: генератор, выдающий описание предоставленных
    для обработки операций.
    """

    data_type_validator(transactions)
    structure_validator(transactions)

    for operation in transactions:
        yield operation["description"]


def card_number_generator(start: int, end: int) -> Generator[str]:
    """
    Функция генерирует номера карт ро шаблону:
    "ХХХХ ХХХХ ХХХХ ХХХХ", где Х - цифра от 0 до 9
    :param start: задает начало интервала генерации
    :param end: задает конец интервала генерации
    :return: генератор, выдающий список номеров карт
    сгенерированных в указанном интервале.
    """

    interval_validator(start, end)

    for num in range(start, end + 1):
        card_st = str(num).rjust(16, "0")
        yield f"{card_st[:4]} {card_st[4:8]} {card_st[8:12]} {card_st[12:16]}"
