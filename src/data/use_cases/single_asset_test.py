from .single_asset import SingleAsset

def test_get_price():
    ticker = 'AAPL'

    single_asset = SingleAsset()
    dict_ticker = single_asset.get_price(ticker)
    print(dict_ticker)
