
from api.enums.engine import CritResult
from api.enums.roll_mode import RollMode
from api.schemas.response.roll_response import RollResponse


def test_roll_20_return_single_roll(dice_roll):
    """
    GIVEN a DiceRoll instance with a d20
    WHEN roll_20 is called
    THEN it should return exactly one roll between 1 and 20
    """

    result: RollResponse = dice_roll.roll_20()

    assert len(result.rolls) == 1
    assert 1 <= result.rolls[0] <= 20
    

def test_roll_20_with_modifier(dice_roll_plus_ten):
    """
    GIVEN a Diceroll instance with a d20 
    AND with a modifier of 10
    WHEN roll_20 is called
    THEN it should return the result between 1 and 20
    AND it should add a modifier of 10 to the total
    """

    result: RollResponse = dice_roll_plus_ten.roll_20()
    assert len(result.rolls) == 1
    assert 1 <= result.rolls[0] <= 20
    assert result.rolls[0] + result.modifier == result.total

def test_roll_20_times_3(dice_roll):
    """
    GIVEN a Diceroll instance with a d20
    AND with a times attribute of 3
    WHEN regular_roll is called
    THEN it should return rolls with len equal to 3
    AND it should add the values to the total
    """

    result: RollResponse = dice_roll.regular_roll(times=3, modifier=0)

    assert len(result.rolls) == 3
    assert sum(result.rolls) == result.total

def test_roll_20_times_4_keep_3(dice_roll, monkeypatch):
    """
    GIVEN a Diceroll instance with a d20
    WHEN roll_and_keep is called
    AND with a times attribute of 4
    AND with a keep attribute of 3
    THEN it should return rolls with len equal to 4
    AND it should return kept with len equal to 3
    AND it should return dropped with len equal to 1
    AND it should add kept values to total
    """

    rolls = [5, 17, 9, 13]

    monkeypatch.setattr(
        dice_roll.dice,
        "roll",
        lambda: rolls.pop(0)
    )

    result: RollResponse = dice_roll.roll_and_keep(times=4, keep=3)

    assert len(result.rolls) == 4
    assert len(result.kept) == 3
    assert len(result.dropped) == 1
    assert result.total == sum(result.kept)