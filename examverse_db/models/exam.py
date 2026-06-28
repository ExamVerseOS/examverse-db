from sqlalchemy import Column, String
from examverse_db.base import Base

class Exam(Base):
    __tablename__ = "exams"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)