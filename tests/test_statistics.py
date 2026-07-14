from typing import Any

import pytest

from data_for_test.statistics.statistics_test_data import (
    statistics_test_invalid_data,
    statistics_test_valid_data,
)
from src.statistics import transactions_by_categories
from src.tools.input_data_formater import param_packer, value_packer


@pytest.mark.parametrize(
    param_packer(statistics_test_valid_data),
    value_packer(statistics_test_valid_data),
)
def test_count_by_descr_positive(
    transaction_data: list[dict[str, Any]],
    count_categories: list[str],
    expected_result: list[dict[str, Any]],
) -> None:
    found_transactions = transactions_by_categories(
        transaction_data, count_categories
    )
    assert found_transactions == expected_result


@pytest.mark.parametrize(
    param_packer(statistics_test_invalid_data),
    value_packer(statistics_test_invalid_data),
)
def test_count_by_descr_negative(
    transaction_data: list[dict[str, Any]],
    count_categories: list[str],
    exception_type: type[Exception],
    system_answer: list[dict[str, Any]],
) -> None:
    with pytest.raises(exception_type) as exc_info:
        transactions_by_categories(transaction_data, count_categories)

    if exception_type == KeyError:
        assert exc_info.value.args[0] == system_answer
    else:
        assert str(exc_info.value) == system_answer
