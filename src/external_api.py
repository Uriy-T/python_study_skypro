import os
from typing import Any

import requests as req
from dotenv import load_dotenv

from src.validators.external_api import (
    data_type_validator,
    structure_validator,
)

load_dotenv()
api_key = os.getenv("API_KEY")


def get_amount(transaction: dict[str, Any]) -> float | None:
    """
    Позволяет получить стоимость переданной операции.
    :param transaction: принимает на вход словарь описывающий операцию
    :return: стоимость операции в рублях. Если сумма в USD или EUR,
    выполняет вызов еднпоинта-конвертера внешнего API для
    конвертации в рубли.
    """
    data_type_validator(transaction, dict)

    structure_validator(transaction["operationAmount"]["currency"], "code")
    structure_validator(transaction["operationAmount"], "amount")

    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    if currency in ["USD", "EUR"]:
        if api_key is None:
            raise ValueError("API_KEY не найден в переменных окружения")
        convert_request = req.get(
            url=f"https://api.apilayer.com/exchangerates_data/convert"
            f"?to=RUB&from={currency}&amount={amount}",
            headers={"apikey": api_key},
        )
        converted_amount = round(float(convert_request.json()["result"]), 2)
        return converted_amount

    elif transaction["operationAmount"]["currency"]["code"] == "RUB":
        return round(float(transaction["operationAmount"]["amount"]), 2)

    else:
        return None
