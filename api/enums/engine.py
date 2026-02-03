from enum import Enum

class CritResult(Enum):
    NONE = 'none'
    SUCCESS = 'critical'
    FAILURE = 'failure'