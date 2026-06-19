def filter_by_currency(transactions: list[dict], currency: str):
    return (operation for operation in transactions if operation['operationAmount']['currency']['name'] == currency)


def transaction_descriptions(transactions: list[dict]):
    for operation in transactions:
        yield operation['description']


def card_number_generator(start: int, end: int):
    for num in range(start, end + 1):
        card_str = str(num).rjust(16, "0")  # rjust — выравнивает вправо, заполняет нулями
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
