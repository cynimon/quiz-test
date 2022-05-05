# todo: аннотации типов сделать красиво
# todo: преобразовть итоговый вариант в json либо вернуть пустой объект
from flask import Flask, request, abort
from Quiz import QuizModel
from api_operation import get_quizz_data, handle_data

app = Flask(__name__)

@app.route('/', methods=["POST"])
def index():
    if request.is_json:
        req_id = QuizModel.max_request()
        amount = request.get_json()["questions_num"]
        if get_quizz_data(amount, req_id):
            handle_data(req_id)
        else:
            abort(500)
    else:
        abort(400)
