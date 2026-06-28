from sqlalchemy import Column, String, Text
from examverse_db.base import Base

class PYQ(Base):
    __tablename__ = "pyqs"

    id = Column(String, primary_key=True)
    exam_id = Column(String, nullable=False)
    question = Column(Text, nullable=False)
    year = Column(String)