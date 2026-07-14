from typing import Any

import pytest

from data_for_test.utils.datasets import (
    get_info_invalid_data,
    get_info_path_invalid_data,
    get_info_valid_data,
)
from src.tools.input_data_formater import param_packer, value_packer
from src.utils import get_transaction_info


@pytest.mark.parametrize(
    param_packer(get_info_valid_data), value_packer(get_info_valid_data)
)
def test_get_transaction_info_positive(
    file_for_read: str, expected_data: list[dict[str, Any]]
) -> None:
    data_from_file = get_transaction_info(file_for_read)
    assert data_from_file == expected_data


@pytest.mark.parametrize(
    param_packer(get_info_path_invalid_data),
    value_packer(get_info_path_invalid_data),
)
def test_get_transaction_info_path_negative(
    path: str, exception_type: type[Exception], expected_value: str
) -> None:
    with pytest.raises(exception_type) as exc_info:
        get_transaction_info(path)
    assert str(exc_info.value) == expected_value


@pytest.mark.parametrize(
    param_packer(get_info_invalid_data), value_packer(get_info_invalid_data)
)
def test_get_transaction_info_negative(
    file_for_read: str, expected_data: list
) -> None:
    data_from_file = get_transaction_info(file_for_read)
    assert data_from_file == expected_data
