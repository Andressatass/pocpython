import ast
from src.domain.use_cases.portfolio import Portfolio as PortfolioInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.single_asset import SingleAsset as SingleAssetInterface

class Portfolio(PortfolioInterface):
    def __init__(self,
                user_repository: UsersRepositoryInterface,
                single_asset: SingleAssetInterface) -> None:
        self.__user_repository = user_repository
        self.__single_asset = single_asset

    def add_ticker(self, ticker_name: str, token: str) -> None:
        user = self.__user_repository.select_user(token)
        new_portfolio = ast.literal_eval(user.wallet)
        new_portfolio.append(ticker_name)
        new_portfolio = str(new_portfolio)

        self.__user_repository.update_user_portfolio(token, new_portfolio)

    def delete_ticker(self, ticker_name: str, token: str) -> None:
        user = self.__user_repository.select_user(token)
        new_portfolio = ast.literal_eval(user.wallet)
        new_portfolio.remove(ticker_name)
        new_portfolio = str(new_portfolio)

        self.__user_repository.update_user_portfolio(token, new_portfolio)

    def check_portfolio(self, token: str) -> list:
        user = self.__user_repository.select_user(token)

        return ast.literal_eval(user.wallet)

    def check_price_today(self, token: str) -> dict:
        user = self.__user_repository.select_user(token)
        portfolio = user.wallet

        portfolio_with_price = {}
        for ticker in portfolio:
            portfolio_with_price[ticker] = self.__single_asset.get_price(ticker)

        return portfolio_with_price
