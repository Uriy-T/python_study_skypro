import pytest

from src.widget import mask_account_card, get_date
from tests.utils.input_data_formater import input_data_formater
from tests.widget.widget_input_data import (
    wdt_input_data_positive,
    wdt_input_data_negative,
    gd_valid_data,
    gd_invalid_data
)


class TestMaskAccountCard:
    @pytest.mark.parametrize(*input_data_formater(wdt_input_data_positive))
    def test_mask_account_card_positive(self,
                                        requisite: str,
                                        masked_requisite: str):
        assert mask_account_card(requisite) == masked_requisite

    @pytest.mark.parametrize(*input_data_formater(wdt_input_data_negative))
    def test_mask_account_card_negative(self,
                                        requisite: str,
                                        system_answer: str,
                                        exception_type: type[Exception]):
        with pytest.raises(exception_type) as exc_info:
            mask_account_card(requisite)
            assert str(exc_info.value) == system_answer


class TestGetDate:
    @pytest.mark.parametrize(*input_data_formater(gd_valid_data))
    def test_get_date_positive(self,
                               date: str,
                               iso_date: str):
        assert get_date(date) == iso_date

    @pytest.mark.parametrize(*input_data_formater(gd_invalid_data))
    def test_get_date_negative(self,
                               date: str,
                               system_answer: str,
                               exception_type: type[Exception]):
        with pytest.raises(exception_type) as exc_info:
            get_date(date)

        if exception_type == KeyError:
            assert exc_info.value.args[0] == system_answer
        else:
            assert str(exc_info.value) == system_answer
