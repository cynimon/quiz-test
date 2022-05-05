from sqlalchemy import create_engine
from sqlalchemy.sql.expression import select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, BigInteger, DateTime
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.functions import max
from sqlalchemy.orm import sessionmaker

db_config = "postgresql://docker:docker@localhost:5432/quiz_db"
db = create_engine(db_config)
Base = declarative_base()

Session = sessionmaker(db)
session = Session()


class QuizModel(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    quiz_id = Column(BigInteger, unique=True)
    quiz_text = Column(String(255))
    quiz_answer = Column(String(255))
    created = Column(DateTime)
    request_id = Column(Integer)

    def __init__(self, quiz_id: int, quiz_text: str, quiz_answer: str, created: str, request_id: str) -> None:
        self.quiz_id = quiz_id
        self.quiz_text = quiz_text
        self.quiz_answer = quiz_answer
        self.created = created
        self.request_id = request_id

    def add_quiz(self) -> int:
        try:
            session.add(self)
            session.commit()
            return 0
        except IntegrityError:
            return 1

    @staticmethod
    def max_request() -> int:
        max_id = session.execute(select(max(QuizModel.request_id))).first()
        return max_id[0] + 1

    @staticmethod
    def get_questions(req_id: int) -> list:
        foo = select(QuizModel.quiz_id,
                     QuizModel.quiz_text,
                     QuizModel.quiz_answer,
                     QuizModel.created).where(QuizModel.request_id == req_id)
        return session.execute(foo).all()


Base.metadata.create_all(db)
