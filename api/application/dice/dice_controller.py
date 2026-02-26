from api.domain.gameplay.dice_roll import DiceRoll
from api.domain.dice.standard_dice import StandardDice

from api.schemas.request.roll_request import RollRequest
from api.schemas.response.roll_response import RollResponse

from api.enums.dice_sides import DiceTypeEnum
from api.enums.roll_mode import RollMode

class DiceController:
    def __init__(self, request: RollRequest):
         self.request = request
         self.dice = StandardDice(sides=request.dice)
         self.roller = DiceRoll(self.dice, request.modifier)
    
    def roll(self) -> RollResponse:
        return self._execute_roll()

    def _execute_roll(self) -> RollResponse:
         match self.request.mode:
              case RollMode.CHECK:
                   return self._roll_20()
              case RollMode.NORMAL:
                   return self._roll_normal()
              case RollMode.ADVANTAGE:
                   return self._roll_advantage()
              case RollMode.DISADVANTAGE:
                   return self._roll_disadvantage()
    
    def _roll_20(self) -> RollResponse:
          return self.roller.roll_20(self.request.modifier)    

    def _roll_normal(self) -> RollResponse:
        if self.request.drop_lowest is not None:
            return self.roller.roll_and_drop(self.request.times, self.request.drop_lowest)
        elif self.request.keep_highest is not None:
            return self.roller.roll_and_keep(self.request.times, self.request.keep_highest)
        else:
            return self.roller.regular_roll(self.request.times, self.request.modifier)
    
    def _roll_advantage(self) -> RollResponse:
         return self.roller.roll_advantage(self.request.modifier)
    
    def _roll_disadvantage(self) -> RollResponse:
         return self.roller.roll_disadvantage(self.request.modifier)
                   
