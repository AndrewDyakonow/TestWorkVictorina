
<h1 align="center">Test Work Victorina</h1>

<h2 align="center"> Тестовое задание </h2>

<div align="center">
    
<div>
    <a href="https://pypi.org/project/gunicorn/"><img alt="Static Badge" src="https://img.shields.io/badge/gunicorn-21.2.0-darkgreen?labelColor=gray"></a>
    <a href="https://pypi.org/project/psycopg/"><img alt="Static Badge" src="https://img.shields.io/badge/psycopg-3.1.12-darkblue?labelColor=lightgray"></a>
    <a href="https://pypi.org/project/pydantic/"><img alt="Static Badge" src="https://img.shields.io/badge/pydantic-2.4.2-darkred?labelColor=gray"></a>
    <a href="https://pypi.org/project/requests/"><img alt="Static Badge" src="https://img.shields.io/badge/requests-2.31.0-darkgreen?labelColor=purple"></a>
    <a href="https://pypi.org/project/uvicorn/"><img alt="Static Badge" src="https://img.shields.io/badge/uvicorn-0.23.2-darkgreen?labelColor=purple"></a>
</div>
<div>
    <a href="https://www.python.org/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python"/></a>
    <a href="https://www.postgresql.org/"><img width="48" height="48" src="https://img.icons8.com/color/48/postgreesql.png" alt="postgreesql"/></a>
    <a href="https://www.docker.com/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker"/></a>
    <a href="https://fastapi.tiangolo.com/"><img width="48" height="48" src="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg" alt=""/></a>
    <a href="https://www.sqlalchemy.org/"><img width="48" height="48" src="https://upload.wikimedia.org/wikipedia/commons/d/d7/SQLAlchemy.svg" alt=""/></a>
</div>

</div>

___

<h2>1. Установка</h2>

1.1 Клонируйте проект:
    
```bash
    git clone git@github.com:AndrewDyakonow/TestWorkVictorina.git
```

1.2 Выполните команду построения докер образа и запуска контейнеров

```bash
    docker-compose up --build
```

и дождаться появления в терминале события:
```html
    app | [] [] [INFO] Application startup complete.
```
___

<h2>2. Работа</h2>

2.1 После запуска контейнеров, по адресу http://127.0.0.1:8800/ будет доступно приложение.

Дальнейшие действия необходимо выполнять либо в API-платформе для разработчиков ``Postman``,
либо с помощью веб-интерфейса Swagger, доступного по адресу http://127.0.0.1:8800/docs/

2.2 Для получения вопросов для викторины, необходимо в теле запроса, в атрибуте ``"questions_num"``, 
указать количество вопросов, которые мы желаем получить от сервера, например:

```html
{
    "questions_num": "5"
}
```
Ответом на запрос будет предыдущий сохранённый вопрос для викторины. При первом запросе вернётся пустой объект.

___

<h2>3. Пример </h2>

 <h3>3.1 POSTMAN </h3>

<img alt="Static Badge" src="images/postman.png">

3.1.1 Вставить ссылку на эндпоинт(http://127.0.0.1:8800/) в поле ввода запроса (Номер 1)
3.1.2 В теле запроса указать параметр "questions_num", содержащий количество вопросов (Номер 2)
3.1.3 Нажать кнопку 'SEND' (Номер 3)
3.1.4 При первом запросе в сессии вернётся пустой объект, после повторного нажатия кнопки 'SEND'
будет выведен результат предыдущего запроса

<h3>3.2 Swagger </h3>

3.2.1 Вставить ссылку на эндпоинт(http://127.0.0.1:8800/) в cтроку поиска, раскрыть выпадающее меню POST запроса
<img alt="Static Badge" src="images/swagger_one.png">

3.2.2 Нажать кнопку "Try it out"
<img alt="Static Badge" src="images/swagger_two.png">

3.2.3 В поле 'Request body' ввести атрибут ``questions_num``, с указанием количества вопросов и нажать кнопку ``Execute``
<img alt="Static Badge" src="images/swagger_three.png">

3.2.4 В итоге в поле ``Server response`` будет отображён результат запроса
<img alt="Static Badge" src="images/swagger_four.png">