from typing import Any

wdt_input_data_positive: list[dict[str, Any]] = [
    {
        "requisite": "Maestro 1596837868705199",
        "masked_requisite": "Maestro 1596 83** **** 5199",
    },
    {
        "requisite": "Счет 64686473678894779589",
        "masked_requisite": "Счет ****9589",
    },
    {
        "requisite": "Visa Platinum 8990922113665229",
        "masked_requisite": "Visa Platinum 8990 92** **** 5229",
    },
]

wdt_input_data_negative: list[dict[str, Any]] = [
    {
        "requisite": " 8990922113665229",
        "system_answer": "Реквизит не соответствует поддерживаемому шаблону.",
        "exception_type": ValueError,
    },
    {
        "requisite": " Счет",
        "system_answer": "Реквизит не соответствует поддерживаемому шаблону.",
        "exception_type": ValueError,
    },
    {
        "requisite": 8990922113665229,
        "system_answer": "Реквизит не является str.",
        "exception_type": TypeError,
    },
    {
        "requisite": 12.521,
        "system_answer": "Реквизит не является str.",
        "exception_type": TypeError,
    },
    {
        "requisite": ["Visa Platinum 8990922113665229"],
        "system_answer": "Реквизит не является str.",
        "exception_type": TypeError,
    },
    {
        "requisite": ("Visa Platinum 8990922113665229",),
        "system_answer": "Реквизит не является str.",
        "exception_type": TypeError,
    },
    {
        "requisite": {"type": "Visa Platinum", "number": 8990922113665229},
        "system_answer": "Реквизит не является str.",
        "exception_type": TypeError,
    },
    {
        "requisite": {"Visa Platinum 8990922113665229"},
        "system_answer": "Реквизит не является str.",
        "exception_type": TypeError,
    },
]

gd_valid_data: list[dict[str, Any]] = [
    {"date": "2024-03-11T02:26:18.671407", "iso_date": "11.03.2024"}
]

gd_invalid_data: list[dict[str, Any]] = [
    {
        "date": "2024-03-1102:26:18.671407",
        "system_answer": "Переданное значение описано не по ISO формату.",
        "exception_type": ValueError,
    },
    {
        "date": 1,
        "system_answer": "Значение не является str.",
        "exception_type": TypeError,
    },
    {
        "date": 51.34,
        "system_answer": "Значение не является str.",
        "exception_type": TypeError,
    },
    {
        "date": True,
        "system_answer": "Значение не является str.",
        "exception_type": TypeError,
    },
    {
        "date": None,
        "system_answer": "Значение не является str.",
        "exception_type": TypeError,
    },
    {
        "date": [1, 2, 3],
        "system_answer": "Значение не является str.",
        "exception_type": TypeError,
    },
    {
        "date": {1, 2, 3},
        "system_answer": "Значение не является str.",
        "exception_type": TypeError,
    },
    {
        "date": (1, 2, 3),
        "system_answer": "Значение не является str.",
        "exception_type": TypeError,
    },
    {
        "date": {"day": 1, "month": 10, "year": 1999},
        "system_answer": "Значение не является str.",
        "exception_type": TypeError,
    },
]
