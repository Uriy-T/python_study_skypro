from typing import Any

import pytest

from data_for_test.table_data_readers.xlsx_reader_test_data import (
    get_info_invalid_data, get_info_path_invalid_data, get_info_valid_data)
from src.table_data_readers import xlsx_reader
from src.tools.input_data_formater import param_packer, value_packer


@pytest.mark.parametrize(
    param_packer(get_info_valid_data), value_packer(get_info_valid_data)
)
def test_get_transaction_xlsx_positive(
        file_for_read: str, expected_data: list[dict[str, Any]]
) -> None:
    data_from_file = xlsx_reader(file_for_read)
    assert data_from_file == expected_data


@pytest.mark.parametrize(
    param_packer(get_info_path_invalid_data),
    value_packer(get_info_path_invalid_data),
)
def test_get_transaction_xlsx_negative(
        path: str, exception_type: type[Exception], expected_value: str
) -> None:
    with pytest.raises(exception_type) as exc_info:
        xlsx_reader(path)
    assert str(exc_info.value) == expected_value


@pytest.mark.parametrize(
    param_packer(get_info_invalid_data), value_packer(get_info_invalid_data)
)
def test_get_transaction_xlsx_path_negative(
        file_for_read: str, expected_data: list
) -> None:
    data_from_file = xlsx_reader(file_for_read)
    assert data_from_file == expected_data
