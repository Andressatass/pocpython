class SingleAssetSpy:
    def __init__(self) -> None:
        self.get_price_atributes = {}

    def get_price(self, ticker_name: str) -> str:
        self.get_price_atributes["ticker_name"] = ticker_name

        return "123"
