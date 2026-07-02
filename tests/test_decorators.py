import pytest
from _pytest.capture import CaptureFixture

from data_for_test.decorators.log_decorator import (log_invalid_data,
                                                    log_valid_data)
from src.decorators import log
from src.processing import filter_by_state
from src.tools.input_data_formater import param_packer, value_packer


@pytest.mark.parametrize(
    param_packer(log_valid_data), value_packer(log_valid_data)
)
def test_log_console_output_positive(
    capsys: CaptureFixture,
    data_for_filter: list[dict],
    log_data: str,
    state: str,
) -> None:
    log()(filter_by_state)(data_for_filter, state=state)
    captured_output = capsys.readouterr()

    assert captured_output.out == log_data


@pytest.mark.parametrize(
    param_packer(log_invalid_data), value_packer(log_invalid_data)
)
def test_log_console_output_negative(
    capsys: CaptureFixture,
    data_for_filter: list[dict],
    log_data: str,
    state: str,
) -> None:
    result = log()(filter_by_state)(data_for_filter, state=state)
    assert "Функция: filter_by_state - ошибка выполнения" in result
    assert log_data in result

    captured_output = capsys.readouterr()
    assert (
        "Функция: filter_by_state - ошибка выполнения" in captured_output.out
    )
    assert log_data in captured_output.out


@pytest.mark.parametrize(
    param_packer(log_valid_data), value_packer(log_valid_data)
)
def test_log_file_output_positive(
    capsys: CaptureFixture,
    data_for_filter: list[dict],
    log_data: str,
    state: str,
) -> None:
    log(filename="event_log.txt")(filter_by_state)(
        data_for_filter, state=state
    )

    with open("event_log.txt", "r", encoding="utf-8") as file:
        log_list = file.read()
        assert log_data in log_list


@pytest.mark.parametrize(
    param_packer(log_invalid_data), value_packer(log_invalid_data)
)
def test_log_file_output_negative(
    capsys: CaptureFixture,
    data_for_filter: list[dict],
    log_data: str,
    state: str,
) -> None:
    log(filename="event_log.txt")(filter_by_state)(
        data_for_filter, state=state
    )

    with open("event_log.txt", "r", encoding="utf-8") as file:
        log_list = file.read()
        assert log_data in log_list
