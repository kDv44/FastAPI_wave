from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Column

from src.database.db_config import Base


class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
    items = relationship("DbArticle", back_populates="users")


class DbArticle(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    published = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("DbUser", back_populates="items")
