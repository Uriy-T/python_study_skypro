def get_mask_card_number(card_number: int) -> str:
    """Функция частично маскИрует номер карты клиента банка.

    :param card_number: принимает номер карты в формате целого числа.
    Длина значения:16 символов.
    :return: возвращает строку с номером карты по маске: XXXX XX** **** XXXX
    """
    str_number = str(card_number)
    return f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"


def get_mask_account(account: int) -> str:
    """Функция частично маскИрует номер счета клиента банка.

    :param account: принимает номер счета клиента
    в формате целого числа из 20 символов.
    :return: возвращает строчное представление номера по маске:
     ****ХХХХ
    """
    return f"**{str(account)[-4:]}"
