from enum import Enum


class RollMode(str, Enum):
    NORMAL = "normal"
    CHECK = "check"
    ADVANTAGE = "advantage"
    DISADVANTAGE = "disadvantage"
