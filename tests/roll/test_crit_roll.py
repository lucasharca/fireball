
from api.enums.engine import CritResult
from api.enums.roll_mode import RollMode
from api.schemas.response.roll_response import RollResponse


def test_roll_20_critical(dice_roll, monkeypatch):
    """
        GIVEN a DiceRoll instance with a d20
        WHEN roll_20 is called and rolls a 20
        THEN the result must be a critical Success
    """
    monkeypatch.setattr(
        dice_roll.dice,
        "roll",
        lambda: 20
    )

    result: RollResponse = dice_roll.roll_20()

    assert result.rolls == [20]
    assert result.total == 20
    assert result.critical == CritResult.SUCCESS
    

def test_roll_20_critical_failure(dice_roll, monkeypatch):
    """
        GIVEN a DiceRoll instance with a d20
        WHEN roll_20 is called and rolls a 1
        THEN the result must be a critical Failure
    """
    monkeypatch.setattr(
        dice_roll.dice,
        "roll",
        lambda: 1
    )

    result: RollResponse = dice_roll.roll_20()

    assert result.rolls == [1]
    assert result.total == 1
    assert result.critical == CritResult.FAILURE