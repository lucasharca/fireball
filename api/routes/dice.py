from fastapi import APIRouter, HTTPException

from api.application.dice.dice_controller import DiceController
from api.schemas.roll_request import RollRequest

router = APIRouter()

@router.post("/roll")
def post_roll(request: RollRequest):
    return DiceController(request).roll()
    