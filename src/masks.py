def get_mask_card_number(card_number: int) -> str:
    """Функция частично маскИрует номер карты клиента банка.

    :param card_number: принимает номер карты клиента в формате целого числа из 16 символов.
    :return: возвращает строчное представление номера по маске: XXXX XX** **** XXXX
    """
    return (
        f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    )


def get_mask_account(account: int) -> str:
    """Функция частично маскИрует номер счета клиента банка.

    :param account: принимает номер счета клиента в формате целого числа из 20 символов.
    :return: возвращает строчное представление номера по маске ****ХХХХ
    """
    return f"**{str(account)[-4:]}"
