import pytest

from api.domain.dice.standard_dice import StandardDice
from api.enums.dice_sides import DiceTypeEnum

from api.domain.gameplay.dice_roll import DiceRoll


@pytest.fixture
def d20():
    return StandardDice(DiceTypeEnum.D20)

@pytest.fixture
def dice_roll(d20):
    return DiceRoll(
        dice=d20, 
        modifier=0
    )

@pytest.fixture
def dice_roll_plus_ten(d20):
    return DiceRoll(
        dice=d20,
        modifier=10
    )
