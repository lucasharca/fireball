from abc import ABC, abstractmethod

class Dice(ABC):
    @abstractmethod
    def roll(self):
        pass