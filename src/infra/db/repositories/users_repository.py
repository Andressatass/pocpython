from typing import List
from src.infra.db.settings.conection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users

class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, id_client: str, name: str, wallet: List, token: str) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    id = id_client,
                    name = name,
                    wallet = wallet,
                    token = token,
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, token: str) -> Users:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session
                        .query(UsersEntity)
                        .filter(UsersEntity.token == token)
                        .first()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def update_user_portfolio(cls, token: str, portfolio: str) -> None:
        with DBConnectionHandler() as database:
            try:
                user = (
                    database.session
                    .query(UsersEntity)
                    .filter(UsersEntity.token == token)
                    .first()
                )
                user.wallet = portfolio
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
