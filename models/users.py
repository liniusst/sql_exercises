# pylint: disable= missing-docstring
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base


class Users(Base):
    __tablename__ = "users"
    id: int = Column(Integer, primary_key=True)
    name: str = Column("Name", String)
    surname: str = Column("Surname", String)
    username: str = Column("Username", String)
    password: str = Column("Password", String)
    tasks = relationship("Tasks", back_populates="users")
