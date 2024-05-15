import ast
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

    portfolio = Portfolio(repo, single_asset)
    portfolio.add_ticker(ticker_name= mocked_ticker, token= mocked_token)

    assert repo.update_user_portfolio_atributes["portfolio"] == "['PETR4', '%s']" %(
        mocked_ticker,
        )

    print(repo.update_user_portfolio_atributes)

@pytest.mark.skip(reason="Sensive test")
def test_delete_ticker():
    mocked_ticker = 'PETR4'
    mocked_token = '54321'

    repo = UsersRepositorySpy()

    single_asset = SingleAsset()

    portfolio = Portfolio(repo, single_asset)
    portfolio.delete_ticker(mocked_ticker, mocked_token)

    assert repo.update_user_portfolio_atributes["portfolio"] == "[]"

    print(repo.update_user_portfolio_atributes)

@pytest.mark.skip(reason="Sensive test")
def test_check_portfolio():
    mocked_token = '123'

    repo = UsersRepositorySpy()

    single_asset = SingleAsset()

    portfolio = Portfolio(repo, single_asset)
    user_portfolio = portfolio.check_portfolio(mocked_token)

    mocked_wallet = ast.literal_eval(repo.select_user_atributes["wallet"])

    assert mocked_wallet == user_portfolio

@pytest.mark.skip(reason="Sensive test")
def test_check_price_today():
    mocked_token = '555'

    repo = UsersRepositorySpy()

    single_asset = SingleAsset()
    mocked_portfolio = {}
    mocked_portfolio['AAPL'] = single_asset.get_price('AAPL')
    mocked_portfolio['GOOGL'] = single_asset.get_price('GOOGL')

    portfolio = Portfolio(repo, single_asset)
    portfolio_dict = portfolio.check_price_today(mocked_token)

    assert mocked_portfolio == portfolio_dict
