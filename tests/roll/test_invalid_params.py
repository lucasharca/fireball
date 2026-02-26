import pytest

from fastapi.testclient import TestClient

from main import app

from api.domain.exceptions import InvalidRollParametersError


client = TestClient(app)


def test_roll_and_keep_invalid_params_raises_domain_error(dice_roll):
    with pytest.raises(InvalidRollParametersError):
        dice_roll.roll_and_keep(times=2, keep=2)


def test_roll_and_drop_invalid_params_raises_domain_error(dice_roll):
    with pytest.raises(InvalidRollParametersError):
        dice_roll.roll_and_drop(times=2, drop=2)


def test_post_roll_invalid_keep_highest_returns_400():
    response = client.post(
        "/dice/roll",
        json={"dice": "D20", "times": 2, "keep_highest": 2, "mode": "normal"},
    )

    assert response.status_code == 422
    body = response.json()
    assert "detail" in body


def test_post_roll_invalid_drop_lowest_returns_400():
    response = client.post(
        "/dice/roll",
        json={"dice": "D20", "times": 2, "drop_lowest": 2, "mode": "normal"},
    )

    assert response.status_code == 422
    body = response.json()
    assert "detail" in body

