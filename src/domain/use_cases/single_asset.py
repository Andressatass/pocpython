from abc import ABC, abstractmethod

class SingleAsset(ABC):

    @abstractmethod
    def get_price(self, ticker_name: str) -> str:
        pass
