from sqlalchemy import Column, String
from src.infra.db.settings.base import Base

class Users(Base):
    __tablename__ = "Users"

    id = Column(String)
    token = Column(String, primary_key=True)
    name = Column(String)
    wallet = Column(String)

    def __repr__(self):
        return f"Users [id={self.id}, name={self.name}, wallet={self.wallet}]"
    