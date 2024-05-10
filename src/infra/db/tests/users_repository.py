from src.domain.models.users import Users

class UsersRepositorySpy:

    def __init__(self) -> None:
        self.insert_user_atributes = {}
        self.select_user_atributes = {}
        self.update_user_portfolio_atributes = {}

    def insert_user(self, id_client: str, name: str, wallet: str, token: str) -> None:
        self.insert_user_atributes["id_client"] = id_client
        self.insert_user_atributes["name"] = name
        self.insert_user_atributes["wallet"] = wallet
        self.insert_user_atributes["token"] = token

    def select_user(self, token: str) -> Users:
        self.select_user_atributes["token"] = token
        return (
            Users(
                name= 'andressa', wallet="{'PETR4': 123}", token= token
            )
        )

    def update_user_portfolio(self, token: str, portfolio: str) -> None:
        self.update_user_portfolio_atributes["token"] = token
        self.update_user_portfolio_atributes["portfolio"] = portfolio
