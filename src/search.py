import re
from typing import Any

from src.validators.base_validator import (
    collection_elements_type_validator,
    data_type_validator,
)


def search_by_descr(
    transactions: list[dict[str, Any]], search_str: str
) -> list[dict[str, Any]]:
    """
    Функция фильтрует транзакции из общего списка
    по переданной подстроке, по частичному совпадению
    :param transactions: Принимает список словарей,
    описывающих транзакции
    :param search_str: Принимает подстроку для
    фильтрации транзакций
    :return: отфильтрованный список объектов
    """
    data_type_validator(transactions, list, "transactions")
    collection_elements_type_validator(transactions, dict, "transactions")
    data_type_validator(search_str, str, "search_str")

    search_filter = re.compile(rf"{search_str.lower()}")

    return [
        transaction
        for transaction in transactions
        if re.search(search_filter, transaction["description"].lower())
    ]
