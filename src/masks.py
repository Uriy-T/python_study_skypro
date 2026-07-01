import logging

mask_card_logger = logging.getLogger("masks.get_mask_card_number")
mask_account_logger = logging.getLogger("masks.get_mask_account")

mask_handler = logging.FileHandler(
    "logs/masks.log", encoding="utf-8", mode="w"
)
mask_formater = logging.Formatter(
    "%(asctime)s-%(name)s-%(levelname)s-%(message)s"
)
mask_handler.setFormatter(mask_formater)

mask_card_logger.addHandler(mask_handler)
mask_card_logger.setLevel(logging.DEBUG)
mask_account_logger.addHandler(mask_handler)
mask_account_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Функция частично маскИрует номер карты клиента банка.

    :param card_number: принимает номер карты в формате целого числа.
    Длина значения:16 символов.
    :return: возвращает строку с номером карты по маске: XXXX XX** **** XXXX
    """

    if not isinstance(card_number, int) or isinstance(card_number, bool):
        mask_card_logger.error("Переданное значение не является int")
        raise TypeError("Переданное значение не является int")
    if card_number <= 0:
        mask_card_logger.error("Переданное число не является положительным")
        raise ValueError("Переданное число не является положительным")

    str_number = str(card_number)
    if len(str_number) != 16:
        mask_card_logger.error("Номер карты должен содержать 16 цифр")
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked_number = (
        f"{str_number[:4]} {str_number[4:6]}** **** {str_number[-4:]}"
    )
    mask_card_logger.info(f"Номер карты успешно замаскирован: {masked_number}")
    return masked_number


def get_mask_account(account: int) -> str:
    """Функция частично маскИрует номер счета клиента банка.

    :param account: принимает номер счета клиента
    в формате целого числа из 20 символов.
    :return: возвращает строчное представление номера по маске:
     ****ХХХХ
    """
    if not isinstance(account, int) or isinstance(account, bool):
        mask_account_logger.error("Переданное значение не является int")
        raise TypeError("Переданное значение не является int")
    if account <= 0:
        mask_account_logger.error("Номер счета не может быть отрицательным")
        raise ValueError("Номер счета не может быть отрицательным")

    str_account = str(account)
    if len(str_account) != 20:
        mask_account_logger.error("Номер счета должен содержать 20 цифр")
        raise ValueError("Номер счета должен содержать 20 цифр")
    masked_account = f"****{str(account)[-4:]}"
    mask_account_logger.info(
        f"Номер счета успешно замаскирован: {masked_account}"
    )
    return masked_account
