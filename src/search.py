import re
from typing import Any


def search_by_descr(
        transactions: list[dict[str, Any]],
        search_str: str
) -> list[dict[str, Any]]:
    search_filter = re.compile(rf'{search_str.lower()}')

    return [transaction for transaction in transactions
            if re.search(search_filter, transaction['description'].lower())]


# test_data = [
#     {
#         "id": 441945886,
#         "state": "EXECUTED",
#         "date": "2019-08-26T10:50:58.294041",
#         "operationAmount": {
#             "amount": "31957.58",
#             "currency": {
#                 "name": "руб.",
#                 "code": "RUB"
#             }
#         },
#         "description": "Пополнение счета",
#         "from": "Maestro 1596837868705199",
#         "to": "Счет 64686473678894779589"
#     },
#     {
#         "id": 41428829,
#         "state": "EXECUTED",
#         "date": "2019-07-03T18:35:29.512364",
#         "operationAmount": {
#             "amount": "8221.37",
#             "currency": {
#                 "name": "USD",
#                 "code": "USD"
#             }
#         },
#         "description": "Списание по кредиту",
#         "from": "MasterCard 7158300734726758",
#         "to": "Счет 35383033474447895560"
#     },
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {
#             "amount": "9824.07",
#             "currency": {
#                 "name": "EUR",
#                 "code": "EUR"
#             }
#         },
#         "description": "Списание по кредиту",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702"
#     }
# ]
#
# print(search_by_descr(transactions=test_data,
#                       search_str='по'))
