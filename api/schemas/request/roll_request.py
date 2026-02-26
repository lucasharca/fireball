from pydantic import BaseModel, Field, model_validator
from typing import Optional

from api.enums.dice_sides import DiceTypeEnum
from api.enums.roll_mode import RollMode


class RollRequest(BaseModel):
    dice: DiceTypeEnum = Field(
        default=DiceTypeEnum.D20,
        description="Type of dice by number of sides (e.g., 6, 20, 100)",
    )
    times: int = Field(default=1, ge=1, description="Number of times to roll the dice (must be >= 1)")
    drop_lowest: Optional[int] = Field(default=None, ge=0, description="Number of low dice to discard")
    keep_highest: Optional[int] = Field(default=None, ge=0, description="Number of higher dice to keep")
    modifier: int = Field(default=0, description="Fixed modifier to add on result")
    mode: RollMode = RollMode.CHECK

    @model_validator(mode="after")
    def validate_keep_drop_vs_times(self) -> "RollRequest":
        if self.drop_lowest is not None and self.keep_highest is not None:
            raise ValueError("drop_lowest and keep_highest cannot be used together")

        if self.drop_lowest is not None and self.drop_lowest >= self.times:
            raise ValueError("drop_lowest must be less than times")

        if self.keep_highest is not None and self.keep_highest >= self.times:
            raise ValueError("keep_highest must be less than times")

        return self