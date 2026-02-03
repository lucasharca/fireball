from api.domain.dice.interfaces.dice import Dice

class DiceRoll():
    def __init__(self, dice: Dice, modifier: int):
        self.dice = dice
        self.modifier = modifier
    
    def _roll(self, times: int = 1) -> list[int]:
        if times < 1:
            raise ValueError("times of rolling must be >= 1")
        
        rolls = []
        for _ in range(times):
            rolls.append(self.dice.roll())

        return rolls
    
    def regular_roll(self, times: int = 1) -> dict:
        rolls = self._roll(times)
        return {
            "total": sum(rolls),
            "result": rolls
        }
    
    def roll_advantage(self) -> dict:
        rolls = self._roll(2)
        return {
            "rolls": rolls,
            "result": max(rolls)
        }
    
    def roll_disadvantage(self) -> dict:
        rolls = self._roll(2)
        return {
            "rolls": rolls,
            "result": min(rolls)
        }
    def roll_and_keep(self, times: int = 2, keep: int = 1) -> dict:
        if times < 1 or keep < 0 or keep >= times:
            raise ValueError("Invalid values for times or keep. Check the rules")
        
        rolls = self._roll(times)
        rolls_sorted = sorted(rolls)
        kept = rolls_sorted[-keep:]
        dropped = rolls_sorted[:-keep]

        return {
            "total": sum(rolls),
            "kept": kept,
            "dropped": dropped
        }

    def roll_and_drop(self, times: int = 2, drop: int = 1) -> dict:
        if times < 1 or drop < 0 or drop >= times:
            raise ValueError("Invalid values for times or drop. Check the rules")
        
        rolls = self._roll(times)
        rolls_sorted = sorted(rolls)
        kept = rolls_sorted[drop:]
        dropped = rolls_sorted[:drop]
        
        return {
            "total": sum(rolls),
            "kept": kept,
            "dropped": dropped
        }
            
