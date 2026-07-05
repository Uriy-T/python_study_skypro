import os
from typing import Any
import csv
import pandas as pd
import logging

csv_transaction_logger = logging.getLogger('table_data_readers.csv_reader')
xlsx_transaction_logger = logging.getLogger('table_data_readers.xlsx_reader')

csv_transaction_logger.setLevel(logging.DEBUG)
xlsx_transaction_logger.setLevel(logging.DEBUG)

transaction_handler = logging.FileHandler(
    "logs/table_data_readers.log", encoding="utf-8", mode="w"
)
transaction_formater = logging.Formatter(
    "%(asctime)s-%(name)s-%(levelname)s-%(message)s")
transaction_handler.setFormatter(transaction_formater)

csv_transaction_logger.addHandler(transaction_handler)
xlsx_transaction_logger.addHandler(transaction_handler)


def csv_reader(path_to_csv: str) -> list[dict[str, Any]]:
    """
        Функция преобразует данные из файлов CSV в python объект:
        список словарей.
        :param path_to_csv: принимает строку с путем
        к файлу, из которого нужно проводить чтение.
        :return: возвращает список словарей с данными о транзакциях
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
            f'Файл пустой или не существует по указанному пути: '
            f'"{path_to_csv}".'
        )
        return []

    with open(path_to_csv, 'r', encoding='utf-8') as file:
        csv_data = csv.DictReader(file, delimiter=';')
        is_content = next(csv_data)
        if is_content:
            csv_transaction_logger.info(
                f'Файл по пути "{path_to_csv}" успешно обработан.'
            )
            return [row for row in csv_data]
        else:
            csv_transaction_logger.error(
                f'Структура данных файла пуста.'
            )
            return []


def xlsx_reader(path_to_xlsx: str) -> list[dict[str, Any]]:
    actual_type = type(path_to_xlsx)
    if actual_type != str:
        xlsx_transaction_logger.error(
            f"Ожидаемый тип данных: str."
            f"Передан тип: {actual_type.__name__}."
        )
        raise TypeError(
            f"Ожидаемый тип данных: str."
            f"Передан тип: {actual_type.__name__}."
        )

    if not os.path.exists(path_to_xlsx) and os.path.getsize(path_to_xlsx) == 0:
        xlsx_transaction_logger.error(
            f'Файл пустой или не существует по указанному пути: '
            f'"{path_to_xlsx}".'
        )
        return []

    xlsx_data = pd.read_excel(path_to_xlsx)
    if not xlsx_data.empty:
        xlsx_transaction_logger.info(
            f'Файл по пути "{path_to_xlsx}" успешно обработан.'
        )
        return [row.to_dict() for _, row in xlsx_data.iterrows()]
    else:
        xlsx_transaction_logger.error(
            f'Структура данных файла пуста.'
        )
        return []
