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
        ticker_price = self.__single_asset.get_price(ticker_name)

        user = self.__user_repository.select_user(token)
        new_portfolio = eval(user.wallet)
        new_portfolio[ticker_name] = ticker_price
        new_portfolio = str(new_portfolio)

        self.__user_repository.update_user_portfolio(token, new_portfolio)

    def delete_ticker(self, ticker_name: str, token: str) -> None:
        user = self.__user_repository.select_user(token)
        new_portfolio = eval(user.wallet)
        del new_portfolio[ticker_name]
        new_portfolio = str(new_portfolio)

        self.__user_repository.update_user_portfolio(token, new_portfolio)

    def check_portfolio(self, token: str) -> dict:
        user = self.__user_repository.select_user(token)
        portfolio = eval(user.wallet)

        return portfolio

##preciso trocar o dict por uma lista, não faz sentido guardar no banco
## os ativos com o spreços, não tem necessidade
