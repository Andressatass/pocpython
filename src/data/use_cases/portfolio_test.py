import pytest
from src.infra.db.tests.users_repository import UsersRepositorySpy
from src.data.use_cases.single_asset import SingleAsset
from .portfolio import Portfolio

@pytest.mark.skip(reason="Sensive test")
def test_add_ticker():
    mocked_ticker = 'AAPL'
    mocked_token = '123456'

    repo = UsersRepositorySpy()

    single_asset = SingleAsset()
    ticker_price = single_asset.get_price(mocked_ticker)

    portfolio = Portfolio(repo, single_asset)
    portfolio.add_ticker(ticker_name= mocked_ticker, token= mocked_token)

    assert repo.update_user_portfolio_atributes["portfolio"] == "{'PETR4': 123, '%s': %s}" %(
        mocked_ticker,
        ticker_price
        )

    print(repo.update_user_portfolio_atributes)
