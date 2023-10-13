from requests import get
from apps.validation import ForDB
from db.distributor import Distributor
from db.models import VictorinaModel


class BusinessLogic:
    """Работа с базой данных"""
    url = 'https://jservice.io/api/random?count='

    def __init__(self, body: int | str):
        """Количество вопросов в запросе"""
        self.body = str(body)

    def get_questions(self) -> list[dict]:
        """Запрос получения вопросов"""
        responce = get(self.url + self.body)
        return responce.json()

    def insert_data(self) -> list[VictorinaModel] | str:
        """Записать данные в БД"""
        condition = True
        count_requests = 0
        while condition:
            count_requests += 1
            data = self.get_questions()
            result = self.data_preparation(data)
            db_request = Distributor()
            condition, last_request = db_request.add_data(result, self.body)

            if count_requests >= 5:
                condition = False
                return 'К сожалению новых вопросов не осталось, попробуйте уменьшить количество вопросов в запросе'
        return last_request

    @staticmethod
    def data_preparation(data):
        """Получить последний запрос"""
        ex_list = []
        for question in data:
            ex_list.append(ForDB(**question))

        return ex_list
