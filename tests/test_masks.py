import pytest

from data_for_test.masks.masks_input_data import (
    account_invalid_data,
    account_valid_data,
    card_invalid_data,
    card_valid_data,
)
from src.masks import get_mask_account, get_mask_card_number
from src.tools.input_data_formater import param_packer, value_packer


@pytest.mark.parametrize(
    param_packer(card_valid_data), value_packer(card_valid_data)
)
def test_mask_card_number_positive(
    card_number: int, masked_value: str
) -> None:
    assert get_mask_card_number(card_number=card_number) == masked_value


@pytest.mark.parametrize(
    param_packer(card_invalid_data), value_packer(card_invalid_data)
)
def test_mask_card_number_negative(
    card_number: int,
    system_answer: str,
    exception_type: type[Exception],
) -> None:
    with pytest.raises(exception_type) as exc_info:
        get_mask_card_number(card_number=card_number)

    if exception_type == KeyError:
        assert exc_info.value.args[0] == system_answer
    else:
        assert str(exc_info.value) == system_answer


@pytest.mark.parametrize(
    param_packer(account_valid_data), value_packer(account_valid_data)
)
def test_account_mask_positive(account: int, masked_value: str) -> None:
    assert get_mask_account(account=account) == masked_value


@pytest.mark.parametrize(
    param_packer(account_invalid_data), value_packer(account_invalid_data)
)
def test_account_mask_negative(
    account: int, system_answer: str, exception_type: type[Exception]
) -> None:
    with pytest.raises(exception_type) as exc_info:
        get_mask_account(account=account)

    if exception_type == KeyError:
        assert exc_info.value.args[0] == system_answer
    else:
        assert str(exc_info.value) == system_answer
