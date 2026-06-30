import sys
from functools import wraps
from typing import Any, Callable


def log(
    filename: str | None = None,
) -> Callable[[Callable], Callable[..., str]]:
    """
    Функция декорирует выполняемые функции функционалом
    по сбору логов о ее выполнении.
    в первой версии логируются:
    - имя исполняемой функции;
    - время начала работы;
    - время окончания работы;
    - результат выполнения ->
    В случае вызова исключения выдает в результате
    текст исключения и введенные данные для диагностики:

    :param filename: принимает путь к файлу для логирования.
    По умолчанию имеет значение None.
    Если не указан, логи транслируются в консоль.
    :return: строку с логами события отработки
    """

    def log_builder(func: Callable) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:

            try:
                result = func(*args, **kwargs)
                log_data = (
                    f"Функция: {func.__name__} - успешно.\n"
                    f"Результат работы:\n"
                    f"{result}\n\n"
                )

                if filename:
                    with open(filename, "a+", encoding="utf-8") as file:
                        file.write(log_data)
                else:
                    sys.stdout.write(log_data)
                return log_data

            except Exception as e:
                log_data = (
                    f"Функция: {func.__name__} - ошибка выполнения.\n"
                    f"Результат работы:\n"
                    f"{e}\n"
                    f"Были введены данные: {args}, {kwargs}\n\n"
                )

                if filename:
                    with open(filename, "a+", encoding="utf-8") as file:
                        file.write(log_data)
                else:
                    sys.stdout.write(log_data)

                return log_data

        return wrapper

    return log_builder
