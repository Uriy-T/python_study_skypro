from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(requisite: str) -> str | None:
    """Функция принимает на вход реквизит клиента банка.
    Применят механизм маскИрования данных, соответствующий типу реквизита.

    :param requisite: принимает строку с данными реквизита клиента
    :return: возвращает замаскИрованную строку с данными реквизита.

    В случае ввода в невалидных, выводит соответствующее ситуации сообщение.
    """
    if not isinstance(requisite, str):
        raise TypeError('Реквизит не является str.')

    if requisite in ['', ' ']:
        raise ValueError('Данные для маскИрования не предоставлены.')

    requisite_type = " ".join(requisite.split()[:-1])
    requisite_number = requisite.split()[-1]

    if not requisite_type or not requisite_number:
        raise ValueError('Реквизит не соответствует поддерживаемому шаблону.')

    if len(requisite_number) == 16:
        int_requisite = int(requisite_number)
        return f"{requisite_type} {get_mask_card_number(int_requisite)}"
    elif len(requisite_number) == 20:
        int_requisite = int(requisite_number)
        return f"{requisite_type} {get_mask_account(int_requisite)}"
    else:
        return "Предоставлен неизвестный тип реквизита."


def get_date(date: str) -> str:
    """Функция преобразует дату в формате ISO 8601 в дату в формате ДД.ММ.ГГГГ.

    :param date: принимает на вход строчное значение даты.
    :return: возвращает строчное значение даты в формате ДД.ММ.ГГГГ
    """
    try:
        return datetime.fromisoformat(date).strftime("%d.%m.%Y")

    except ValueError:
        raise ValueError('Переданное значение описано не по ISO формату.')

    except TypeError:
        raise TypeError('Значение не является str.')
