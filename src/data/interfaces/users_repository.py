from typing import List
from typing import Dict
from abc import ABC, abstractmethod
from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, id_client: str, name: str, wallet: Dict, token: str) -> None: pass

    @abstractmethod
    def select_user(self, token: str) -> List[Users]: pass

    @abstractmethod
    def update_user_portfolio(self, token: str, portfolio: Dict) -> None: pass
            