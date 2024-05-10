from typing import List

class Users:
    def __init__(self, name: str, wallet: List, token: str) -> None:
        self.name = name
        self.wallet = wallet
        self.token = token
