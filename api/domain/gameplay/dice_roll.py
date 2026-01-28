from api.domain.dice.interfaces.dice import Dice

class DiceRoll():
    def __init__(self, dice: Dice):
        self.dice = dice
    
    def roll(self, times: int = 1) -> list[int]:
        if times < 1:
            raise ValueError("times of rolling must be >= 1")
        
        rolls = []
        for _ in range(times):
            rolls.append(self.dice.roll())

        return rolls

    def roll_and_remove(self, times: int = 2, drop: int = 1) -> dict:
        if times < 1 or drop < 0 or drop >= times:
            raise ValueError("Invalid values for times or drop. Check the rules")
        
        rolls = self.roll(times)
        rolls_sorted = sorted(rolls)
        kept = rolls_sorted[drop:]
        dropped = rolls_sorted[:drop]
        
        return {
            "kept": kept,
            "dropped": dropped
        }
            
