import json
import logging
import os.path
from typing import Any

transaction_logger = logging.getLogger("utils.get_transaction_info")
transaction_logger.setLevel(logging.DEBUG)
transaction_handler = logging.FileHandler(
    "logs/utils.log", encoding="utf-8", mode="w"
)
transaction_formater = logging.Formatter(
    "%(asctime)s-%(name)s-%(levelname)s-%(message)s"
)
transaction_handler.setFormatter(transaction_formater)
transaction_logger.addHandler(transaction_handler)


def get_transaction_info(path_to_json: str) -> list[dict[str, Any]]:
    """
    Производит чтение данных о банковских операциях из внешнего
    json файла.
    :param path_to_json: принимает путь к файлу с данными для чтения
    :return: python-объект с данными об операциях
    """

    actual_type = type(path_to_json)
    if actual_type != str:
        transaction_logger.error(
            f"Переданный путь к файлу не является строкой."
            f"передано значение типа {actual_type.__name__}"
        )
        raise TypeError(
            f"Ожидаемый тип данных: str."
            f"Передан тип: {actual_type.__name__}."
        )

    if not os.path.exists(path_to_json) or os.path.getsize(path_to_json) == 0:
        transaction_logger.error(
            f'Файл пустой или не существует по указанному пути: '
            f'"{path_to_json}".'
        )
        return []

    with open(path_to_json, "r", encoding="utf-8") as data:
        content = json.load(data)
        if not isinstance(content, list):
            return []
        else:
            transaction_logger.info(
                f'Файл по пути "{path_to_json}" успешно обработан.'
            )
            return content
