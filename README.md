# quiz-test
___

### Что делает

- Принимает на вход запрос типа {"questions_num": integer};
- Получает с публичного API указанное количество вопросов из банка данных;
- Записывает вопросы в БД с учетом уникальности вопроса - при совпадении вопросов происходит перезапрос;
- Возвращает ответ на запрос: те вопросы, которые были запрошены в предыдущий запрос к API.

### Запуск

- Перед запуском, пожалуйста, убедитесь, что порт 5432 не занят локальной версией PostgreSQL
```shell
$ sudo netstat -tulnp | grep :5432
$ sudo kill <номер рядом с postgres, 
            если окажется, что порт им занят>
```

- После клонирования проекта с GitHub, в терминале корневой папки (quiz_test):
```shell
$ docker-compose up -d 
```
- После запуска контейнеров, находим ID контейнера в приложением и находим, на каком IP-адресе он работает:
```shell
$ docker ps
$ docker inspect <container id> | grep "IPAddress"
```
- Отправляем запросы формата (ниже) на адрес (через Postman, например):
```shell
<IPAdress>:5000/

{
  "questions_num": <число>
}
```
- Для остановки контейнеров:
```shell
$ docker-compose stop
```
- Для полного удаления контейнеров и папок данных:
```shell
$ docker-compose down --volumes
```

### Примеры
- После запуска контейнеров, отправка POST-запросов на адрес:
```json
{
  "questions_num": 1
}
```
- Ответ:
```json
{
    "quizzes": {}
}
```
- Второй запрос
```json
{
  "questions_num": 0
}
```
- Ответ
```json
{
    "quizzes": [
        {
            "created": "Thu, 22 Jan 2015 02:33:17 GMT",
            "quiz_answer": "birth",
            "quiz_id": 146384,
            "quiz_text": "After seeing a video about removing a stuck wine cork, Jorge Odon invented a medical device to ease this process"
        }
    ]
}
```
- Третий запрос
```json
{
  "questions_num": 2
}
```
- Ответ
```json
{
    "quizzes": {}
}
```