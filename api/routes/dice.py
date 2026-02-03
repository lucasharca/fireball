from fastapi import APIRouter

from api.application.dice.dice_controller import DiceController
from api.schemas.request.roll_request import RollRequest

from api.schemas.response.roll_response import RollResponse

router = APIRouter()

@router.post("/roll", response_model=RollResponse)
def post_roll(request: RollRequest):
    result = DiceController(request).roll()
    return result
    