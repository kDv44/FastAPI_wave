from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import Column

from src.database.db_config import Base


class DbUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
