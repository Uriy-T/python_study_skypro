def input_data_formater(data: list[dict[str, str]]) -> list[str | list[tuple[str]]]:
    """Функция принимает на вход набор данных представляющий собой список словарей.
    И переформатирует его в конструкцию, которую ожидает получить для работы фикстура
    @pytest.mark.parametrize.

    :param data: список словарей содержащих параметры ввода
    :return: список содержащий строку состоящую из имен параметров ввода
    и список кортежей с самими значениями ввода.
    """

    param_pack = list(data[0].keys())
    value_pack = [tuple(item.values()) for item in data]

    return [', '.join(param_pack), value_pack]
