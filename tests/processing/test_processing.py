import pytest

from src.processing import filter_by_state, sort_by_date
from tests.processing.filter_by_state_test_data import (
    fbs_invalid_data,
    fbs_valid_data,
    fbs_valid_data_partial,
)
from tests.processing.sort_by_date_test_data import (
    sdb_invalid_data,
    sdb_valid_data,
    sdb_valid_data_partial,
)
from tests.utils.input_data_formater import param_packer, value_packer


class TestFilterByState:

    @pytest.mark.parametrize(
        param_packer(fbs_valid_data), value_packer(fbs_valid_data)
    )
    def test_filter_by_state_positive(
        self,
        data_for_filter: list[dict],
        state: str,
        filtered_list: list[dict],
    ) -> None:
        assert filter_by_state(data_for_filter, state) == filtered_list

    @pytest.mark.parametrize(
        param_packer(fbs_valid_data_partial),
        value_packer(fbs_valid_data_partial),
    )
    def test_filter_by_state_positive_partial(
        self, data_for_filter: list[dict], filtered_list: list[dict]
    ) -> None:
        assert filter_by_state(data_for_filter) == filtered_list

    @pytest.mark.parametrize(
        param_packer(fbs_invalid_data), value_packer(fbs_invalid_data)
    )
    def test_filter_by_state_negative(
        self,
        data_for_filter: list[dict],
        state: str,
        system_answer: str,
        exception_type: type[Exception],
    ) -> None:
        with pytest.raises(exception_type) as exc_info:
            filter_by_state(data_for_filter, state)

        if exception_type == KeyError:
            assert exc_info.value.args[0] == system_answer
        else:
            assert str(exc_info.value) == system_answer


class TestSortByDate:

    @pytest.mark.parametrize(
        param_packer(sdb_valid_data), value_packer(sdb_valid_data)
    )
    def test_sort_by_date_positive(
        self,
        data_for_sort: list[dict],
        sort_order: bool,
        sorted_list: list[dict],
    ) -> None:
        assert sort_by_date(data_for_sort, sort_order) == sorted_list

    @pytest.mark.parametrize(
        param_packer(sdb_valid_data_partial),
        value_packer(sdb_valid_data_partial),
    )
    def test_x_positive_partial(
        self, data_for_sort: list[dict], sorted_list: list[dict]
    ) -> None:
        assert sort_by_date(data_for_sort) == sorted_list

    @pytest.mark.parametrize(
        param_packer(sdb_invalid_data), value_packer(sdb_invalid_data)
    )
    def test_sort_by_date_negative(
        self,
        data_for_sort: list[dict],
        sort_order: bool,
        system_answer: str,
        exception_type: type[Exception],
    ) -> None:
        with pytest.raises(exception_type) as exc_info:
            sort_by_date(data_for_sort, sort_order)

        if exception_type == KeyError:
            assert exc_info.value.args[0] == system_answer
        else:
            assert str(exc_info.value) == system_answer
