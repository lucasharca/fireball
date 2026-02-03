from enum import Enum

class RollMode(str, Enum):
    NORMAL = 'normal' 
    ADVANTAGE = 'advantage'
    DISAVANTAGE = 'disavantage'
