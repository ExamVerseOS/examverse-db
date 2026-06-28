from sqlalchemy import Column, String
from examverse_db.base import Base

class Topic(Base):
    __tablename__ = "topics"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    exam_id = Column(String, nullable=False)
    subject_id = Column(String, nullable=True)
    type = Column(String, default="topic")