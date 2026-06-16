import pytest

from src.masks import get_mask_account, get_mask_card_number
from tests.masks.masks_input_data import (
    account_invalid_data,
    account_valid_data,
    card_invalid_data,
    card_valid_data,
)
from tests.utils.input_data_formater import param_packer, value_packer


class TestCardMask:

    @pytest.mark.parametrize(
        param_packer(card_valid_data), value_packer(card_valid_data)
    )
    def test_mask_card_number_positive(
        self, card_number: int, masked_value: str
    ) -> None:
        assert get_mask_card_number(card_number=card_number) == masked_value

    @pytest.mark.parametrize(
        param_packer(card_invalid_data), value_packer(card_invalid_data)
    )
    def test_mask_card_number_negative(
        self,
        card_number: int,
        system_answer: str,
        exception_type: type[Exception],
    ) -> None:
        with pytest.raises(exception_type, match=system_answer):
            get_mask_card_number(card_number=card_number)


class TestAccountMask:

    @pytest.mark.parametrize(
        param_packer(account_valid_data), value_packer(account_valid_data)
    )
    def test_account_mask_positive(
        self, account: int, masked_value: str
    ) -> None:
        assert get_mask_account(account=account) == masked_value

    @pytest.mark.parametrize(
        param_packer(account_invalid_data), value_packer(account_invalid_data)
    )
    def test_account_mask_negative(
        self, account: int, system_answer: str, exception_type: type[Exception]
    ) -> None:
        with pytest.raises(exception_type, match=system_answer):
            get_mask_account(account=account)
