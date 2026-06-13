import pytest

from src.masks import get_mask_account, get_mask_card_number
from tests.utils.input_data_formater import input_data_formater
from tests.masks.masks_input_data import (
    card_valid_data,
    card_invalid_data,
    account_valid_data,
    account_invalid_data
)


class TestCardMask:

    @pytest.mark.parametrize(*input_data_formater(card_valid_data))
    def test_mask_card_number_positive(self,
                                       card_number: int,
                                       masked_value: str):
        assert get_mask_card_number(card_number=card_number) == masked_value

    @pytest.mark.parametrize(*input_data_formater(card_invalid_data))
    def test_mask_card_number_negative(self,
                                       card_number: int,
                                       system_answer: str,
                                       exception_type: type[Exception]):
        with pytest.raises(exception_type, match=system_answer):
            get_mask_card_number(card_number=card_number)


class TestAccountMask:

    @pytest.mark.parametrize(*input_data_formater(account_valid_data))
    def test_account_mask_positive(self,
                                   account: int,
                                   masked_value: str):
        assert get_mask_account(account=account) == masked_value

    @pytest.mark.parametrize(*input_data_formater(account_invalid_data))
    def test_account_mask_negative(self,
                                   account: int,
                                   system_answer: str,
                                   exception_type: type[Exception]):
        with pytest.raises(exception_type, match=system_answer):
            get_mask_account(account=account)
