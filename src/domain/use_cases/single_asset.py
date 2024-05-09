from abc import ABC, abstractmethod
from typing import Dict

class SingleAsset(ABC):

    @abstractmethod
    def get_price(self, ticker_name: str) -> Dict:
        pass

class SingleAssetUseCase(SingleAsset):

    def get_price(self, ticker_name: str) -> Dict:
        ##logica
        pass