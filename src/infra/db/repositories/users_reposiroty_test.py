import pytest
from sqlalchemy import text
from src.infra.db.settings.conection import DBConnectionHandler
from .users_repository import UsersRepository

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()

@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    portfolio = {}
    mocked_id = '123'
    mocked_name = 'name'
    mocked_wallet = portfolio
    mocked_token = 'oqbjdfbdjf'

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_id, mocked_name, mocked_wallet, mocked_token)

    sql = '''
        SELECT * FROM Users
        WHERE name = '{}'
        AND id = '{}'
        AND token = '{}'
    '''.format(mocked_name, mocked_id, mocked_token)
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.id == mocked_id
    assert registry.name == mocked_name
    assert registry.token == mocked_token

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {registry.id}
    '''))
    connection.commit()

@pytest.mark.skip(reason="Sensive test")
def test_select_user():
    portfolio = {}
    mocked_id = '1234'
    mocked_name = 'name2'
    mocked_wallet = portfolio
    mocked_token = 'oqb'

    sql = '''
        INSERT INTO users (id, name, wallet, token) VALUES ('{}','{}','{}','{}')
    '''.format(mocked_id, mocked_name, mocked_wallet, mocked_token)
    connection.execute(text(sql))
    connection.commit()

    users_repository = UsersRepository()
    response = users_repository.select_user(mocked_token)

    assert response[0].id == mocked_id
    assert response[0].name == mocked_name
    assert response[0].wallet == mocked_wallet
    assert response[0].token == mocked_token

    connection.execute(text(f'''
        DELETE FROM users WHERE id = {response[0].id}
    '''))
    connection.commit()

@pytest.mark.skip(reason="Sensive test")
def test_update_user_portfolio():
    portfolio = {}
    mocked_id = '1234'
    mocked_name = 'name2'
    mocked_wallet = portfolio
    mocked_token = 'token1'

    sql = '''
        INSERT INTO users (id, name, wallet, token) VALUES ('{}','{}','{}','{}')
    '''.format(mocked_id, mocked_name, mocked_wallet, mocked_token)
    connection.execute(text(sql))
    connection.commit()

    new_portfolio = {'falso dict'}

    users_repository = UsersRepository()
    users_repository.update_user_portfolio('token1', new_portfolio)
