from typing import Any, Generator

from src.valodators.generators_validators import (
    currency_validator,
    data_type_validator,
    interval_validator,
    structure_validator,
)


def filter_by_currency(
    transactions: list[dict], currency: str
) -> Generator[dict[Any, Any], None, None]:
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
    data_type_validator(transactions)
    structure_validator(transactions)

    for operation in transactions:
        yield operation["description"]


def card_number_generator(start: int, end: int) -> Generator[str]:
    interval_validator(start, end)

    for num in range(start, end + 1):
        card_st = str(num).rjust(16, "0")
        yield f"{card_st[:4]} {card_st[4:8]} {card_st[8:12]} {card_st[12:16]}"
