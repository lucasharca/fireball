from api.domain.gameplay.dice_roll import DiceRoll
from api.domain.dice.standard_dice import StandardDice

from api.enums.dice_sides import DiceTypeEnum

class DiceController:
    def roll(self, sides: int, times: int = 1) -> dict:
        new_dice = StandardDice(sides=DiceTypeEnum(sides))
        rolls = DiceRoll(dice=new_dice).roll(times=times)
        
        return {
            "dice": f"d{sides}",
            "rolls":  rolls,
            "total": sum(rolls)
        }
    
    def roll_drop(self, sides: int, drop: int, times: int = 1,) -> dict:
        new_dice = StandardDice(sides=DiceTypeEnum(sides))
        rolls = DiceRoll(dice=new_dice).roll_and_remove(times=times, drop=drop)

        print(rolls)

        return {
            "dice": f"d{sides}",
            "kept": rolls["kept"],
            "dropped": rolls["dropped"]
        }
        
        
