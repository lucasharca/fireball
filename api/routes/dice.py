from fastapi import APIRouter, HTTPException

from api.application.dice.dice_controller import DiceController

router = APIRouter()

@router.get("/roll")
def dice_roll(sides: int, times: int = 1):
    return DiceController().roll(sides=sides, times=times)

@router.get("/roll/drop")
def dice_roll_drop(sides: int,  drop: int, times: int = 1):
    return DiceController().roll_drop(sides=sides, drop=drop, times=times)
