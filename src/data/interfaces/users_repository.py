from abc import ABC, abstractmethod
from typing import List
from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, id_client: str, name: str, wallet: List, token: str) -> None: pass

    @abstractmethod
    def select_user(self, token: str) -> Users: pass

    @abstractmethod
    def update_user_portfolio(self, token: str, portfolio: str) -> None: pass
            