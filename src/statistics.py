from collections import defaultdict
from typing import Any

from src.validators.base_validator import (
    collection_elements_type_validator,
    data_type_validator,
)


def transactions_by_categories(
    transactions: list[dict[str, Any]], categories: list[str]
) -> dict[str, int]:
    """
    Функция считает количество операций по указанному
    списку категорий (поле description)
    :param transactions: принимает список объектов,
    описывающих транзакции.
    :param categories: принимает список строк, по
    которым происходит подсчет. Подсчет ведется
    по полному совпадению значения категории
    :return: словарь со списком категорий и количества
    операций, им соответствующих
    """

    data_type_validator(transactions, list, "transactions")
    collection_elements_type_validator(transactions, dict, "transactions")
    data_type_validator(categories, list, "categories")
    collection_elements_type_validator(categories, str, "categories")

    transactions_count: dict[str, int] = defaultdict(int)

    for category in categories:
        transactions_count[category]
        for transaction in transactions:
            if transaction["description"].lower() == category.lower():
                transactions_count[category] += 1

    return dict(transactions_count)
