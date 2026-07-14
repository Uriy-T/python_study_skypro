from typing import Any, Hashable

from config import available_states
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.search import search_by_descr
from src.table_data_readers import csv_reader, xlsx_reader
from src.utils import get_transaction_info
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Исполняет основную логику программы.
    Позволяет выбрать источник данных об операциях и
    проводить контроль выводимых в итоге списков
    транзакций.
    """

    available_states_lower = [status.lower() for status in available_states]

    while True:
        try:
            choose_source_data = int(
                input(
                    "Привет! Добро пожаловать в программу работы "
                    "с банковскими транзакциями.\n"
                    "Выберите необходимый пункт меню введя номер операции:\n"
                    "1. Получить информацию о транзакциях из JSON-файла\n"
                    "2. Получить информацию о транзакциях из CSV-файла\n"
                    "3. Получить информацию о транзакциях из XLSX-файла\n"
                    "Ответ: "
                )
            )
            break

        except ValueError:
            print(
                "Введенное значение не может быть интерпретировано"
                " как целочисленное."
            )

    while choose_source_data not in [1, 2, 3]:
        choose_source_data = int(
            input(
                "Выбранная операция не поддерживается.\n"
                "Выберите необходимый пункт меню введя номер операции:\n"
                "1. Получить информацию о транзакциях из JSON-файла\n"
                "2. Получить информацию о транзакциях из CSV-файла\n"
                "3. Получить информацию о транзакциях из XLSX-файла\n"
                "Ответ: "
            )
        )

    if choose_source_data == 1:
        print("Для обработки выбран JSON-файл.")
        transaction_data = get_transaction_info("data/operations_main.json")

    if choose_source_data == 2:
        print("Для обработки выбран CSV-файл.")
        transaction_data: list[dict[Hashable, Any]] = csv_reader(
            "data/operations_main.csv"
        )

    if choose_source_data == 3:
        print("Для обработки выбран XLSX-файл.")
        transaction_data: list[dict[Hashable, Any]] = xlsx_reader(
            "data/operations_main.xlsx"
        )

    choose_status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        f"Доступные для фильтрации статусы: {available_states}\n"
        f"Ответ: "
    ).lower()

    while True:
        if choose_status in available_states_lower:
            filter_by_state_data = filter_by_state(
                transaction_data, state=choose_status
            )
            print(f'Операции отфильтрованы по статусу "{choose_status}"')
            break
        else:
            print(f'Статус операции "{choose_status}" недоступен.')
            choose_status = input(
                "Введите статус, по которому необходимо"
                " выполнить фильтрацию.\n"
                f"Доступные для фильтрации статусы: {available_states}"
            ).lower()

    is_sort_by_date = input(
        "Отсортировать операции по дате? Да/Нет\n" "Ответ: "
    ).lower()

    while True:
        if is_sort_by_date == "да":
            choose_sort_order = input(
                "Отсортировать по возрастанию или по убыванию?\n" "Ответ: "
            ).lower()
            if choose_sort_order in "по убыванию":
                sorted_dy_date_data = sort_by_date(
                    filter_by_state_data, sort_order=True
                )
                break
            elif choose_sort_order in "по возрастанию":
                sorted_dy_date_data = sort_by_date(
                    filter_by_state_data, sort_order=False
                )
                break
            else:
                print("Введен не ожидаемый вариант ответа.")

        elif is_sort_by_date == "нет":
            sorted_dy_date_data = filter_by_state_data
            break
        else:
            print("Введен не ожидаемый вариант ответа.")
            is_sort_by_date = input(
                "Отсортировать операции по дате? Да/Нет\n" "Ответ: "
            ).lower()

    rub_operation_output = input(
        "Выводить только рублевые транзакции? Да/Нет\n" "Ответ: "
    )
    while True:
        if rub_operation_output == "да":
            filter_by_currency_data = list(
                filter_by_currency(sorted_dy_date_data, currency="RUB")
            )

            break
        elif rub_operation_output == "нет":
            filter_by_currency_data = sorted_dy_date_data
            break
        else:
            print("Введен не ожидаемый вариант ответа.")
            rub_operation_output = input(
                "Выводить только рублевые транзакции? Да/Нет\n" "Ответ: "
            )

    filter_by_descr = input(
        "Отфильтровать список транзакций по определенному"
        "слову в описании? Да/Нет\n"
        "Ответ: "
    )

    while True:
        if filter_by_descr == "да":
            keyword_for_filter = input("Введите текст для фильтрации: ")
            result_output_data = search_by_descr(
                transactions=filter_by_currency_data,
                search_str=keyword_for_filter,
            )
            break
        elif filter_by_descr == "нет":
            result_output_data = filter_by_currency_data
            break
        else:
            print("Введен не ожидаемый вариант ответа.")
            filter_by_descr = input(
                "Отфильтровать список транзакций по определенному"
                " слову в описании? Да/Нет\n"
                "Ответ: "
            )

    print("Распечатываю итоговый список транзакций...\n")

    result_transaction_count = len(result_output_data)

    if result_transaction_count > 0:
        print(
            f"Всего банковских операций"
            f" в выборке: {result_transaction_count}\n"
        )
        descriptions = transaction_descriptions(result_output_data)

        for transaction in result_output_data:

            print(f"{get_date(transaction['date'])} " f"{next(descriptions)}")
            if "Перевод" in transaction["description"]:
                print(
                    f"{mask_account_card(transaction['from'])}"
                    f" -> {mask_account_card(transaction['to'])}"
                )
            else:
                print(f"{mask_account_card(transaction['to'])}")
            if choose_source_data == 1:
                print(
                    f"Сумма: {transaction['operationAmount']['amount']} "
                    f"{transaction['operationAmount']['currency']['name']}\n"
                )
            elif choose_source_data in [2, 3]:
                print(
                    f"Сумма: {transaction['amount']} "
                    f"{transaction['currency_name']}\n"
                )

    else:
        print(
            "Не найдено ни одной транзакции,"
            " подходящей под ваши условия фильтрации."
        )


if __name__ == "__main__":
    main()
