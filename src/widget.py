from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(requisite: str) -> str | None:
    """Функция принимает на вход реквизит клиента банка и в зависимости от типа применят соответствующий механизм
    маскИрования данных.

    :param requisite: принимает строку с данными реквизита клиента
    :return: возвращает строку с замаскИрованными данными в зависимости от типа клиента. В случае подачи данных в
    невалидном формате или реквизита не известного типа, выводит соответствующее сообщение.
    """
    if requisite and isinstance(requisite, str):
        requisite_type = ' '.join(requisite.split()[:-1])
        requisite_number = requisite.split()[-1]

        if len(requisite_number) == 16:
            return f'{requisite_type} {get_mask_card_number(int(requisite_number))}'
        elif len(requisite_number) == 20:
            return f'{requisite_type} {get_mask_account(int(requisite_number))}'
        else:
            return 'Предоставлен неизвестный тип реквизита клиента'
    else:
        return 'Предоставлены неверные данные. Проверьте правильность ввода данных'


def get_date(date: str) -> str:
    """Функция преобразует дату в формате ISO 8601 в дату в формате ДД.ММ.ГГГГ.

    :param date: принимает на вход строчное значение даты в формате ISO 8601
    :return: возвращает строчное значение даты в формате ДД.ММ.ГГГГ
    """
    date_elems = reversed(date.split('T')[0].split('-'))
    return '.'.join(date_elems)
