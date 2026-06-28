from sqlalchemy import Column, String
from examverse_db.base import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    exam_id = Column(String, nullable=False)