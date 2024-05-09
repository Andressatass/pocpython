import yfinance as yf
from src.domain.use_cases.single_asset import SingleAsset as SingleAssetInterface

class SingleAsset(SingleAssetInterface):
    def __init__(self) -> None:
        pass

    def get_price(self, ticker_name: str) -> str:
        ticker = yf.Ticker(ticker_name)
        ticker_info = ticker.info
        return ticker_info['currentPrice']
