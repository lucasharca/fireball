from api.domain.dice.interfaces.dice import Dice

class DiceRoll():
    def __init__(self, dice: Dice, times: int = 1):
        self.dice = dice
        self.times = times 
    
    def roll(self) -> list[int]:
        rolls = []
        for i in range(self.times):
            rolls.append(self.dice.roll())

        return rolls

