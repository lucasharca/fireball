from api.domain.dice.standard_dice import StandardDice
from api.enums.engine import CritResult
from api.enums.roll_mode import RollMode
from api.schemas.response.roll_response import RollResponse
class DiceRoll():
    def __init__(self, dice: StandardDice, modifier: int):
        self.dice = dice
        self.modifier = modifier
    
    def _roll(self, times: int = 1) -> list[int]:
        if times < 1:
            raise ValueError("times of rolling must be >= 1")
        
        rolls = []
        for _ in range(times):
            rolls.append(self.dice.roll())

        return rolls
    
    def _verify_crit(self, roll: int) -> CritResult:
        if roll == 20:
            return CritResult.SUCCESS
        elif roll == 1:
            return CritResult.FAILURE
        else:
            return CritResult.NONE

    def _build_response(
            self, 
            dice: int = 20, 
            times: int = 1, 
            rolls: list[int] = [],
            kept: list[int] = [],
            dropped: list[int] = [],
            modifier: int = 0,
            total: int = 0,
            mode: RollMode = RollMode.CHECK,
            critical: CritResult = CritResult.NONE
            ) -> RollResponse:
        response = RollResponse(
            dice=dice,
            times=times,
            rolls=rolls,
            kept=kept,
            dropped=dropped,
            modifier=modifier,
            total=total,
            mode=mode,
            critical=critical
        )

        return response
    
    def roll_20(self, modifier: int = 0) -> RollResponse: 
        roll = self._roll()
        total_result = sum(roll) + modifier

        return self._build_response(
            dice=20, 
            modifier=modifier, 
            rolls=roll, 
            total=total_result,
            critical=self._verify_crit(roll[0])
        )
      

    def regular_roll(self, times: int = 1, modifier: int = 0) -> RollResponse:
        rolls = self._roll(times)
        total_result = sum(rolls) + modifier

        return self._build_response(
            dice=self.dice.sides,
            rolls=rolls, 
            times=times, 
            total=total_result,
            modifier=modifier,

            mode=RollMode.NORMAL,
        )
    
    def roll_advantage(self, modifier: int = 0) -> RollResponse:
        rolls = self._roll(2)
        kept=[max(rolls)]
        dropped=[min(rolls)]

        return self._build_response(
            dice=self.dice.sides, 
            rolls=rolls, 
            kept=kept, 
            dropped=dropped,
            modifier=modifier,
            total=sum(kept) + modifier,
            critical=self._verify_crit(kept[0]),
            mode=RollMode.ADVANTAGE,
        )
    
    def roll_disadvantage(self, modifier: int = 0) -> RollResponse:
        rolls = self._roll(2)
        kept=[min(rolls)]
        dropped=[max(rolls)] 

        return self._build_response(
            dice=self.dice.sides, 
            rolls=rolls, 
            kept=kept,
            dropped=dropped,
            total=sum(kept) + modifier, 
            critical=self._verify_crit(kept[0]),
            modifier=modifier,
            mode=RollMode.DISAVANTAGE,
        )
    
    def roll_and_keep(self, times: int = 2, keep: int = 1) -> RollResponse:
        if times < 1 or keep < 0 or keep >= times:
            raise ValueError("Invalid values for times or keep. Check the rules")
        
        rolls = self._roll(times)
        rolls_sorted = sorted(rolls)
        kept = rolls_sorted[-keep:]
        dropped = rolls_sorted[:-keep]
        return self._build_response(
            dice=self.dice.sides, 
            times=times,
            rolls=rolls, 
            kept=kept,
            dropped=dropped, 
            total=sum(kept),
            mode=RollMode.NORMAL,
        )
    
    def roll_and_drop(self, times: int = 2, drop: int = 1) -> RollResponse:
        if times < 1 or drop < 0 or drop >= times:
            raise ValueError("Invalid values for times or drop. Check the rules")
        
        rolls = self._roll(times)
        rolls_sorted = sorted(rolls)
        kept = rolls_sorted[drop:]
        dropped = rolls_sorted[:drop]
        
        return self._build_response(
            dice=self.dice.sides, 
            times=times,
            rolls=rolls, 
            kept=kept,
            dropped=dropped, 
            total=sum(kept),
            mode=RollMode.NORMAL,
        )
            
