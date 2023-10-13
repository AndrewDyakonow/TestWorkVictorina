from fastapi import FastAPI, Body

from apps.business import BusinessLogic

app = FastAPI()


@app.post('/')
def hello(data=Body()):
    """Эндпоинт"""
    body = data['questions_num']
    processing = BusinessLogic(body)
    result = processing.insert_data()
    return result
