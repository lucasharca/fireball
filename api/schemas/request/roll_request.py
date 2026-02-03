from pydantic import BaseModel, Field
from typing import Optional

from api.enums.roll_mode import RollMode

class RollRequest(BaseModel):
    dice: int = Field(default=20, description="Type of dice by number of sides, ex: 6, 20")
    times: int = Field(default=1, description="Number of times to roll the dice")
    drop_lowest: Optional[int] = Field(default=None, ge=0, description="Number of low dice to discard")
    keep_highest: Optional[int] = Field(default=None, ge=0, description="Number of higher dice to keep")
    modifier: int = Field(default=0, description="Fixed modifier to add on result")
    mode: RollMode = RollMode.CHECK