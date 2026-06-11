from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(requisite: str) -> str | None:
    """Функция принимает на вход реквизит клиента банка.
    Применят механизм маскИрования данных, соответствующий типу реквизита.

    :param requisite: принимает строку с данными реквизита клиента
    :return: возвращает замаскИрованную строку с данными реквизита.

    В случае ввода в невалидных, выводит соответствующее ситуации сообщение.
    """
    if requisite and isinstance(requisite, str):
        requisite_type = " ".join(requisite.split()[:-1])
        requisite_number = requisite.split()[-1]

        if len(requisite_number) == 16:
            int_requisite = int(requisite_number)
            return f"{requisite_type} {get_mask_card_number(int_requisite)}"
        elif len(requisite_number) == 20:
            int_requisite = int(requisite_number)
            return f"{requisite_type} {get_mask_account(int_requisite)}"
        else:
            return "Предоставлен неизвестный тип реквизита клиента"
    else:
        return "Предоставлены неверные данные. Проверьте правильность ввода"


def get_date(date: str) -> str:
    """Функция преобразует дату в формате ISO 8601 в дату в формате ДД.ММ.ГГГГ.

    :param date: принимает на вход строчное значение даты в формате ISO 8601
    :return: возвращает строчное значение даты в формате ДД.ММ.ГГГГ
    """
    return datetime.fromisoformat(date).strftime("%d.%m.%Y")
