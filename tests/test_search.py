from typing import Any

import pytest

from data_for_test.search.search_test_data import (
    search_test_invalid_data,
    search_test_valid_data,
)
from src.search import search_by_descr
from src.tools.input_data_formater import param_packer, value_packer


@pytest.mark.parametrize(
    param_packer(search_test_valid_data), value_packer(search_test_valid_data)
)
def test_search_by_descr_positive(
    transaction_data: list[dict[str, Any]],
    search_string: str,
    expected_result: list[dict[str, Any]],
) -> None:
    found_transactions = search_by_descr(transaction_data, search_string)
    assert found_transactions == expected_result


@pytest.mark.parametrize(
    param_packer(search_test_invalid_data),
    value_packer(search_test_invalid_data),
)
def test_search_by_descr_negative(
    transaction_data: list[dict[str, Any]],
    search_string: str,
    exception_type: type[Exception],
    system_answer: list[dict[str, Any]],
) -> None:
    with pytest.raises(exception_type) as exc_info:
        search_by_descr(transaction_data, search_string)

    if exception_type == KeyError:
        assert exc_info.value.args[0] == system_answer
    else:
        assert str(exc_info.value) == system_answer
