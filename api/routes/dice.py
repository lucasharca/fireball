from fastapi import APIRouter, HTTPException
from api.domain.gameplay.dice_roll import DiceRoll
from api.domain.dice.standard_dice import StandardDice

from api.enums.dice_sides import DiceTypeEnum

router = APIRouter()

@router.get("/roll")
def dice_rool(sides: int, times: int = 1):
    try:
        dice_type = DiceTypeEnum(sides)
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid dice type: d{sides}"
        )
    
    new_dice = StandardDice(sides=dice_type)
    roll_dice = DiceRoll(dice=new_dice, times=times)

    message = roll_dice.roll()
    
    return {f"rolling: {message}"}