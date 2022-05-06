from flask import Flask, request, abort
from Quiz import QuizModel
from api_operation import get_quizz_data, handle_data

app = Flask(__name__)


@app.route('/', methods=["POST"])
def index() -> dict:
    if request.is_json:
        req_id = QuizModel.max_request()
        amount = request.get_json()
        if get_quizz_data(amount["questions_num"], req_id):
            return {"quizzes": handle_data(req_id)}
        else:
            abort(500)
    else:
        abort(400)


if __name__ == "__main__":
    app.run()
