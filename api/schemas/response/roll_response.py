from pydantic import BaseModel
from typing import List, Optional

from api.enums.roll_mode import RollMode
from api.enums.engine import CritResult

class RollResponse(BaseModel):
    dice: int
    times: int

    rolls: List[int]
    kept: List[int]
    dropped: List[int]

    modifier: int
    total: int

    mode: RollMode
    critical: CritResult
