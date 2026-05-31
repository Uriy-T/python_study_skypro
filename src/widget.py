from masks import get_mask_account, get_mask_card_number

def mask_account_card(requisite: str) -> str|None:
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




