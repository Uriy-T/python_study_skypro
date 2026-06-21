from typing import Any


def param_packer(data: list[dict[str, Any]]) -> str:
    return ", ".join(list(data[0].keys()))


def value_packer(data: list[dict[str, Any]]) -> list[tuple]:
    return [tuple(item.values()) for item in data]
