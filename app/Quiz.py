from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, BigInteger, DateTime
from sqlalchemy.exc import IntegrityError

Base = declarative_base()


class QuizModel(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    quiz_id = Column(BigInteger, unique=True)
    quiz_text = Column(String(255))
    quiz_answer = Column(String(255))
    created = Column(DateTime)
    request_id = Column(Integer)

    def __init__(self, quiz_id, quiz_text, quiz_answer, created, request_id):
        self.quiz_id = quiz_id
        self.quiz_text = quiz_text
        self.quiz_answer = quiz_answer
        self.created = created
        self.request_id = request_id

    def add_quiz(self, session):
        try:
            session.add(self)
            session.commit()
            return 0
        except IntegrityError:
            return 1





