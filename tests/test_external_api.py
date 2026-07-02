import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

from data_for_test.external_api.external_test_data import (
    ext_api_invalid_data, ext_api_valid_data, structure_test_data)
from src.external_api import get_amount
from src.tools.input_data_formater import param_packer, value_packer

load_dotenv()
api_key = os.getenv("API_KEY")


@pytest.mark.parametrize(
    param_packer(ext_api_valid_data), value_packer(ext_api_valid_data)
)
@patch("src.external_api.req.get")
def test_get_amount_api_call_positive(
    mock_request: Mock, operation: dict, expected_value: float
) -> None:
    currency_from = operation["operationAmount"]["currency"]["code"]
    amount = operation["operationAmount"]["amount"]
    if operation["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        mock_request.return_value.json.return_value = {
            "result": expected_value
        }
        assert get_amount(operation) == expected_value
        mock_request.assert_called_once_with(
            url=f"https://api.apilayer.com/exchangerates_data/convert"
            f"?to=RUB&from={currency_from}&amount={amount}",
            headers={"apikey": api_key},
        )
    elif operation["operationAmount"]["currency"]["code"] == "RUB":
        assert get_amount(operation) == expected_value


@pytest.mark.parametrize(
    param_packer(ext_api_invalid_data), value_packer(ext_api_invalid_data)
)
@patch("src.external_api.req.get")
def test_get_amount_api_call_negative(
    mock_request: Mock, operation: dict, result: str, expected_value: str
) -> None:
    currency_from = operation["operationAmount"]["currency"]["code"]
    amount = operation["operationAmount"]["amount"]
    if operation["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        mock_request.return_value.json.return_value = {"result": result}
        assert get_amount(operation) == expected_value
        mock_request.assert_called_once_with(
            url=f"https://api.apilayer.com/exchangerates_data/convert"
            f"?to=RUB&from={currency_from}&amount={amount}",
            headers={"apikey": api_key},
        )


@pytest.mark.parametrize(
    param_packer(structure_test_data), value_packer(structure_test_data)
)
def test_get_amount_structure_negative(
    operation: dict, exception_type: type[Exception], expected_value: str
) -> None:
    with pytest.raises(exception_type) as exc_info:
        get_amount(operation)

    if exception_type == KeyError:
        assert exc_info.value.args[0] == expected_value
    else:
        assert str(exc_info.value) == expected_value
