import requests as r
from Quiz import QuizModel


# стягивание данных с API сайта с вопросами, выделение нужных данных для добавление в БД
def get_quizz_data(amount: int, req_id: int) -> bool:
    raw_data = r.get(f'https://jservice.io/api/random?count={amount}').json()
    quiz_data = {'quiz_id': [], 'quiz_text': [], 'quiz_answer': [], 'created': [], 'request_id': req_id}
    for d in raw_data:
        quiz_data['quiz_id'].append(d['id'])
        quiz_data['quiz_text'].append(d['question'])
        quiz_data['quiz_answer'].append(d['answer'])
        quiz_data['created'].append(d['created_at'])
    return add_quizz_to_db(quiz_data, amount)


# добавление данных в базу, если данные уже есть - набор кэша и запуск цикла добавления заново
def add_quizz_to_db(data: dict, amount: int) -> bool:
    count = 0
    for i in range(amount):
        new_quiz = QuizModel(data['quiz_id'][i],
                             data['quiz_text'][i],
                             data['quiz_answer'][i],
                             data['created'][i],
                             data['request_id'])
        count += new_quiz.add_quiz()
    if count > 0:
        get_quizz_data(count, data['request_id'])
    else:
        return True


# выдаёт сохраненные вопросы из предыдущего POST запроса к API
# если запроса не было - то возвращается пустой объект
def handle_data(req_id: int) -> list:
    data_list = QuizModel.get_questions(req_id - 1)
    datas_dict = []
    if len(data_list) == 0:
        return {}
    else:
        for rw in data_list:
            datas_dict.append(QuizModel.to_json(rw))
        return datas_dict
