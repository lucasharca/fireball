from api.domain.gameplay.dice_roll import DiceRoll
from api.domain.dice.standard_dice import StandardDice

from api.schemas.roll_request import RollRequest

from api.enums.dice_sides import DiceTypeEnum
from api.enums.roll_mode import RollMode

class DiceController:
    def __init__(self, request: RollRequest):
         self.request = request
         self.dice = StandardDice(sides=DiceTypeEnum(request.dice))
         self.roller = DiceRoll(self.dice, request.modifier or 0)
    
    def roll(self) -> dict:
        return self._execute_roll()

    def _execute_roll(self) -> dict:
         match self.request.mode:
              case RollMode.NORMAL:
                   return self._roll_normal()
              case RollMode.ADVANTAGE:
                   return self._roll_advantage()
              case RollMode.DISAVANTAGE:
                   return self._roll_disadvantage()
                   
    def _roll_normal(self) -> dict:
        if self.request.drop_lowest is not None:
            return self.roller.roll_and_drop(self.request.times, self.request.drop_lowest)
        elif self.request.keep_highest is not None:
            return self.roller.roll_and_keep(self.request.times, self.request.keep_highest)
        else:
            return self.roller.regular_roll(self.request.times)
    
    def _roll_advantage(self) -> dict:
         return self.roller.roll_advantage()
    
    def _roll_disadvantage(self) -> dict:
         return self.roller.roll_disadvantage()
                   
