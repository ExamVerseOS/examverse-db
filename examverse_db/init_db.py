from examverse_db.base import Base
from examverse_db.session import engine

from examverse_db.models import exam, subject, topic, pyq, user

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ ExamVerseDB initialized successfully")

if __name__ == "__main__":
    init_db()