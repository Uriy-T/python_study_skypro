import csv
import logging
import os
from typing import Any, Hashable

import pandas as pd

csv_transaction_logger = logging.getLogger("table_data_readers.csv_reader")
xlsx_transaction_logger = logging.getLogger("table_data_readers.xlsx_reader")

csv_transaction_logger.setLevel(logging.DEBUG)
xlsx_transaction_logger.setLevel(logging.DEBUG)

transaction_handler = logging.FileHandler(
    "logs/table_data_readers.log", encoding="utf-8", mode="w"
)
transaction_formater = logging.Formatter(
    "Время вызова: %(asctime)s\n"
    "Модуль: %(name)s\n"
    "Серьезность: %(levelname)s\n"
    "Описание события: %(message)s\n"
)
transaction_handler.setFormatter(transaction_formater)

csv_transaction_logger.addHandler(transaction_handler)
xlsx_transaction_logger.addHandler(transaction_handler)


def csv_reader(path_to_csv: str) -> list[dict[str, Any]]:
    """
    Функция преобразует данные из файлов CSV в python объект:
    список словарей.
    :param path_to_csv: принимает строку с путем
    к файлу, из которого нужно проводить чтение.
    :return: возвращает список словарей с данными о транзакциях.
    """

    actual_type = type(path_to_csv)
    if actual_type != str:
        csv_transaction_logger.error(
            f"Ожидаемый тип данных: str."
            f"Передан тип: {actual_type.__name__}."
        )
        raise TypeError(
            f"Ожидаемый тип данных: str."
            f"Передан тип: {actual_type.__name__}."
        )

    if not os.path.exists(path_to_csv) or os.path.getsize(path_to_csv) == 0:
        csv_transaction_logger.error(
            f"Файл пустой или не существует по указанному пути: "
            f'"{path_to_csv}".'
        )
        return []

    with open(path_to_csv, "r", encoding="utf-8") as file:
        csv_data = csv.DictReader(file, delimiter=";")

        is_content = list(csv_data)

        if is_content:
            correct_transactions = []
            for item in is_content:
                for key, value in item.items():
                    if key == "id":
                        item[key] = int(value)
                        correct_transactions.append(item)
            csv_transaction_logger.info(
                f'Файл по пути "{path_to_csv}" успешно обработан.'
            )
            return is_content
        else:
            csv_transaction_logger.error(
                f'Файл по пути "{path_to_csv}" содержит только заголовки.'
            )
            return []


def xlsx_reader(path_to_xlsx: str) -> list[dict[Hashable, Any]] | None:
    """
    Функция преобразует данные из XLSX файла в python объект:
    список словарей.
    :param path_to_xlsx: принимает строку с путем
    к файлу, из которого нужно проводить чтение.
    :return: возвращает список словарей с данными о транзакциях.
    """
    actual_type = type(path_to_xlsx)
    if actual_type != str:
        xlsx_transaction_logger.error(
            f"Неверный путь."
            f"Ожидаемый тип данных: str."
            f"Передан тип: {actual_type.__name__}."
        )
        raise TypeError(
            f"Ожидаемый тип данных: str."
            f"Передан тип: {actual_type.__name__}."
        )

    if not os.path.exists(path_to_xlsx) or os.path.getsize(path_to_xlsx) == 0:
        xlsx_transaction_logger.error(
            f"Файл пустой или не существует по указанному пути: "
            f'"{path_to_xlsx}".'
        )
        return []

    xlsx_data = pd.read_excel(path_to_xlsx, header=None)
    if len(xlsx_data) == 0:
        xlsx_transaction_logger.error(
            f'Файл по пути "{path_to_xlsx}" полностью пуст'
        )
        return []
    elif len(xlsx_data) == 1:
        xlsx_transaction_logger.error(
            f'В файле по пути "{path_to_xlsx}" есть только заголовки.'
        )
        return []

    xlsx_data = pd.read_excel(path_to_xlsx, header=0)
    if not xlsx_data.empty:
        xlsx_transaction_logger.info(
            f'Файл по пути "{path_to_xlsx}" успешно обработан.'
        )

        return [row.to_dict() for _, row in xlsx_data.iterrows()]
    else:
        return []
