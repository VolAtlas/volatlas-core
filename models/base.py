from abc import ABC, abstractmethod

class VolModel(ABC):

    @abstractmethod
    def implied_vol(self, strike: float, maturity: float) -> float:
        pass

