def get_mask_card_number(card_number: int) -> str:
    """Функция частично маскИрует номер карты клиента банка.

    :param card_number: принимает номер карты в формате целого числа.
    Длина значения:16 символов.
    :return: возвращает строку с номером карты по маске: XXXX XX** **** XXXX
    """

    if not isinstance(card_number, int) or isinstance(card_number, bool):
        raise TypeError("Переданное значение не является int")
    if card_number <= 0:
        raise ValueError("Переданное число не является положительным")

    str_number = str(card_number)
    if len(str_number) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")
    return f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"


def get_mask_account(account: int) -> str:
    """Функция частично маскИрует номер счета клиента банка.

    :param account: принимает номер счета клиента
    в формате целого числа из 20 символов.
    :return: возвращает строчное представление номера по маске:
     ****ХХХХ
    """
    if not isinstance(account, int) or isinstance(account, bool):
        raise TypeError("Переданное значение не является int")
    if account <= 0:
        raise ValueError("Номер счета не может быть отрицательным")

    str_account = str(account)
    if len(str_account) != 20:
        raise ValueError("Номер счета должен содержать 20 цифр")
    return f"****{str(account)[-4:]}"
