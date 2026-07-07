from collections import defaultdict
from typing import Any


def transactions_by_categories(
        transactions: list[dict[str, Any]],
        categories: list[str]
) -> dict[str, int]:
    transactions_count = defaultdict(int)

    for category in categories:
        transactions_count[category]
        for transaction in transactions:
            if transaction['description'].lower() == category.lower():
                transactions_count[category] += 1

    return dict(transactions_count)


test_data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Пополнение счета",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Списание по кредиту",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Списание по кредиту",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }
]

print(transactions_by_categories(test_data, ['Списание по кредиту', 'Перевод дивидендов', 'Пополнение счета']))
