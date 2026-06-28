from sqlalchemy import Column, String
from examverse_db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)