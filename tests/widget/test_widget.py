import pytest

from src.widget import get_date, mask_account_card
from tests.utils.input_data_formater import param_packer, value_packer
from tests.widget.widget_input_data import (
    gd_invalid_data,
    gd_valid_data,
    wdt_input_data_negative,
    wdt_input_data_positive,
)


class TestMaskAccountCard:
    @pytest.mark.parametrize(
        param_packer(wdt_input_data_positive),
        value_packer(wdt_input_data_positive),
    )
    def test_mask_account_card_positive(
        self, requisite: str, masked_requisite: str
    ) -> None:
        assert mask_account_card(requisite) == masked_requisite

    @pytest.mark.parametrize(
        param_packer(wdt_input_data_negative),
        value_packer(wdt_input_data_negative),
    )
    def test_mask_account_card_negative(
        self,
        requisite: str,
        system_answer: str,
        exception_type: type[Exception],
    ) -> None:
        with pytest.raises(exception_type) as exc_info:
            mask_account_card(requisite)
            assert str(exc_info.value) == system_answer


class TestGetDate:
    @pytest.mark.parametrize(
        param_packer(gd_valid_data), value_packer(gd_valid_data)
    )
    def test_get_date_positive(self, date: str, iso_date: str) -> None:
        assert get_date(date) == iso_date

    @pytest.mark.parametrize(
        param_packer(gd_invalid_data), value_packer(gd_invalid_data)
    )
    def test_get_date_negative(
        self, date: str, system_answer: str, exception_type: type[Exception]
    ) -> None:
        with pytest.raises(exception_type) as exc_info:
            get_date(date)

        if exception_type == KeyError:
            assert exc_info.value.args[0] == system_answer
        else:
            assert str(exc_info.value) == system_answer
