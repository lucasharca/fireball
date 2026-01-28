import random
from api.domain.dice.interfaces.dice import Dice
from api.enums.dice_sides import DiceTypeEnum

class StandardDice(Dice):
    def __init__(self, sides: DiceTypeEnum) -> None:
        super().__init__()
        self.sides = sides.value
    
    def roll(self):
        return random.randint(1, self.sides)