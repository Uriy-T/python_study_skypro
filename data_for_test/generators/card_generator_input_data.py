from typing import Any

card_gen_valid_data: list[dict[str, Any]] = [

    {'start': 1,
     'end': 5,
     'expected_nums':
         [
             '0000 0000 0000 0001',
             '0000 0000 0000 0002',
             '0000 0000 0000 0003',
             '0000 0000 0000 0004',
             '0000 0000 0000 0005'
         ]
     },

    {'start': 1,
     'end': 12,
     'expected_nums':
         [
             '0000 0000 0000 0001',
             '0000 0000 0000 0002',
             '0000 0000 0000 0003',
             '0000 0000 0000 0004',
             '0000 0000 0000 0005',
             '0000 0000 0000 0006',
             '0000 0000 0000 0007',
             '0000 0000 0000 0008',
             '0000 0000 0000 0009',
             '0000 0000 0000 0010',
             '0000 0000 0000 0011',
             '0000 0000 0000 0012'
         ]
     }
]

card_gen_invalid_data: list[dict[str, Any]] = [

    {'start': 'т',
     'end': 5,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: str\n"
                      f"end: int",
     'exception_type': TypeError
     },

    {'start': 1.156,
     'end': 12,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: float\n"
                      f"end: int",
     'exception_type': TypeError
     },

    {'start': False,
     'end': 12,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: bool\n"
                      f"end: int",
     'exception_type': TypeError
     },

    {'start': None,
     'end': 12,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: NoneType\n"
                      f"end: int",
     'exception_type': TypeError
     },

    {'start': [1, 2, 3],
     'end': 12,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: list\n"
                      f"end: int",
     'exception_type': TypeError
     },

    {'start': (1, 2, 3),
     'end': 12,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: tuple\n"
                      f"end: int",
     'exception_type': TypeError
     },

    {'start': {1, 2, 3},
     'end': 12,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: set\n"
                      f"end: int",
     'exception_type': TypeError
     },

    {'start': {'num1': 1, 'num2': 2, 'num3': 3},
     'end': 12,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: dict\n"
                      f"end: int",
     'exception_type': TypeError
     },

    {'start': 1,
     'end': 'строка',
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: int\n"
                      f"end: str",
     'exception_type': TypeError
     },

    {'start': 1,
     'end': 12.27,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: int\n"
                      f"end: float",
     'exception_type': TypeError
     },

    {'start': 1,
     'end': True,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: int\n"
                      f"end: bool",
     'exception_type': TypeError
     },

    {'start': 1,
     'end': None,
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: int\n"
                      f"end: NoneType",
     'exception_type': TypeError
     },

    {'start': 1,
     'end': [1, 2, 3],
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: int\n"
                      f"end: list",
     'exception_type': TypeError
     },

    {'start': 1,
     'end': (1, 2, 3),
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: int\n"
                      f"end: tuple",
     'exception_type': TypeError
     },

    {'start': 1,
     'end': {1, 2, 3},
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: int\n"
                      f"end: set",
     'exception_type': TypeError
     },

    {'start': 1,
     'end': {'num1': 1, 'num2': 2, 'num3': 3},
     'system_answer': f"Значения и start и end должны быть int."
                      f"Предоставлены типы:\n"
                      f"start: int\n"
                      f"end: dict",
     'exception_type': TypeError
     },
]
