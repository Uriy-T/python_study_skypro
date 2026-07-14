from typing import Type

import pytest

from data_for_test.generators.card_generator_input_data import (
    card_gen_invalid_data,
    card_gen_valid_data,
)
from data_for_test.generators.description_input_data import (
    descr_invalid_data,
    descr_valid_data,
)
from data_for_test.generators.filter_input_data import (
    trans_invalid_data,
    trans_valid_data,
)
from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)
from src.tools.input_data_formater import param_packer, value_packer


@pytest.mark.parametrize(
    param_packer(trans_valid_data), value_packer(trans_valid_data)
)
def test_filter_by_currency_positive(
    transaction: list[dict], currency: str, expected_seq: list[dict]
) -> None:
    filtered_data = list(filter_by_currency(transaction, currency))
    assert filtered_data == expected_seq


# @pytest.mark.parametrize(
#     param_packer(trans_invalid_data), value_packer(trans_invalid_data)
# )
# def test_filter_by_currency_negative(
#     transaction: list[dict],
#     currency: str,
#     system_answer: str,
#     exception_type: type[Exception],
# ) -> None:
#     with pytest.raises(exception_type) as exc_info:
#         filter_by_currency(transaction, currency)
#
#     if exception_type == KeyError:
#         assert exc_info.value.args[0] == system_answer
#     else:
#         assert str(exc_info.value) == system_answer


@pytest.mark.parametrize(
    param_packer(descr_valid_data), value_packer(descr_valid_data)
)
def test_transaction_descriptions_positive(
    transaction: list[dict], expected_seq: list[dict]
) -> None:
    descriptions = transaction_descriptions(transaction)
    descriptions_list = []
    for item in range(6):
        descriptions_list.append(next(descriptions))
    assert descriptions_list == expected_seq


# @pytest.mark.parametrize(
#     param_packer(descr_invalid_data), value_packer(descr_invalid_data)
# )
# def test_transaction_descriptions_negative(
#     transaction: list[dict],
#     system_answer: str,
#     exception_type: Type[Exception],
# ) -> None:
#     gen = transaction_descriptions(transaction)
#     with pytest.raises(exception_type) as exc_info:
#         next(gen)
#
#     if exception_type == KeyError:
#         assert exc_info.value.args[0] == system_answer
#     else:
#         assert str(exc_info.value) == system_answer


@pytest.mark.parametrize(
    param_packer(card_gen_valid_data), value_packer(card_gen_valid_data)
)
def test_card_number_generator_positive(
    start: int, end: int, expected_nums: list[str]
) -> None:
    generated_card_nums = []
    for card_number in card_number_generator(start, end):
        generated_card_nums.append(card_number)
    assert generated_card_nums == expected_nums


@pytest.mark.parametrize(
    param_packer(card_gen_invalid_data), value_packer(card_gen_invalid_data)
)
def test_card_number_generator_negative(
    start: int, end: int, system_answer: str, exception_type: type[Exception]
) -> None:
    gen = card_number_generator(start, end)
    with pytest.raises(exception_type) as exc_info:
        next(gen)

    if exception_type == KeyError:
        assert exc_info.value.args[0] == system_answer
    else:
        assert str(exc_info.value) == system_answer
