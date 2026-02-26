from api.enums.engine import CritResult
from api.enums.roll_mode import RollMode
from api.schemas.response.roll_response import RollResponse

def test_roll_20_advantage(dice_roll, monkeypatch):
    """
    GIVEN two forced results 5 and 17 
    WHEN rolling with advantage
    THEN total must be 17
    """

    rolls = [5, 17]
    
    monkeypatch.setattr(
        dice_roll.dice,
        "roll",
        lambda: rolls.pop(0)
    )

    result: RollResponse = dice_roll.roll_advantage()

    assert result.rolls == [5, 17]
    assert result.kept == [17]
    assert result.dropped == [5]
    assert result.total == 17
    assert result.mode == RollMode.ADVANTAGE
    assert result.critical == CritResult.NONE

def test_roll_20_advantage_with_crit(dice_roll, monkeypatch):
    """
    GIVEN two forced results 5 and 20 
    WHEN rolling with advantage
    THEN total must be 20
    AND critical must be SUCCESS
    """
    rolls = [5, 20]
    
    monkeypatch.setattr(
        dice_roll.dice,
        "roll",
        lambda: rolls.pop(0)
    )

    result: RollResponse = dice_roll.roll_advantage()

    assert result.rolls == [5, 20]
    assert result.kept == [20]
    assert result.dropped == [5]
    assert result.total == 20
    assert result.mode == RollMode.ADVANTAGE
    assert result.critical == CritResult.SUCCESS

def test_roll_20_disadvantage(dice_roll, monkeypatch):
    """
    GIVEN two forced results 5 and 17 
    WHEN rolling with disadvantage
    THEN total must be 5
    """

    rolls = [5, 17]
    
    monkeypatch.setattr(
        dice_roll.dice,
        "roll",
        lambda: rolls.pop(0)
    )

    result: RollResponse = dice_roll.roll_disadvantage()

    assert result.rolls == [5, 17]
    assert result.kept == [5]
    assert result.dropped == [17]
    assert result.total == 5
    assert result.mode == RollMode.DISADVANTAGE
    assert result.critical == CritResult.NONE