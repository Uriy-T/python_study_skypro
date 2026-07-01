import json
import os.path
from typing import Any

from src.validators.get_info_validators import path_type_validator


def get_transaction_info(path_to_data: str) -> list[dict[str, Any]]:
    """
    Производит чтение данных о банковских операциях из внешнего
    json файла.
    :param path_to_data: принимает путь к файлу с данными для чтения
    :return: python-объект с данными об операциях
    """
    path_type_validator(path_to_data, str)

    if not os.path.exists(path_to_data) or os.path.getsize(path_to_data) == 0:
        return []

    with open(path_to_data, "r", encoding="utf-8") as data:
        content = json.load(data)
        if not isinstance(content, list):
            return []
        else:
            return content
