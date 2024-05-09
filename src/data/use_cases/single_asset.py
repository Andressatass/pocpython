from typing import Dict
from src.domain.use_cases.single_asset import SingleAsset as SingleAssetInterface
import yfinance as yf

class SingleAsset(SingleAssetInterface):
    def __init__(self) -> None:
        pass

    def get_price(self, ticker_name: str) -> Dict:
        ticker = yf.Ticker(ticker_name)
        ticker_info = ticker.info
        print(ticker_info)
