from typing import List
from abc import ABC, abstractmethod
from src.domain.models.users import Users

class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, id_client: str, name: str, wallet: str, token: str) -> None: pass

    @abstractmethod
    def select_user(self, token: str) -> any: List[Users]
            