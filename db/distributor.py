from apps.validation import ForDB
from db.db_engine import settings
from db.models import mapper_registry, VictorinaModel
from db.db_session import session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select


class Distributor:
    last_request = 0

    def __init__(self):
        """Создать таблицу, если её ещё нет"""
        mapper_registry.metadata.create_all(settings.create_engine, checkfirst=True)

    @staticmethod
    def add_data(data: list[ForDB], count_question: int) -> tuple[bool, list[VictorinaModel] | None]:
        """Добавить данные в БД"""

        last_re = Distributor.get_data()
        Distributor.last_request = count_question
        with session() as sessions:
            for obj in data:
                b = obj.__dict__
                worker = VictorinaModel(**b)
                sessions.add(worker)
            try:
                sessions.commit()
            except IntegrityError:
                print('Вопрос уже есть в БД, пробуем ещё')
                return True, None
        return False, last_re

    @classmethod
    def get_data(cls) -> list[VictorinaModel]:
        """Получить последний сохранённый вопрос"""
        stmt = select(VictorinaModel).order_by(VictorinaModel.id.desc()).limit(cls.last_request)
        with session() as sessions:
            list_request = [i[0] for i in sessions.execute(stmt)]

        return list_request

