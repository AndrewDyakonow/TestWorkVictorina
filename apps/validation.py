from datetime import datetime
from re import sub
from pydantic import BaseModel, Field
from pydantic.class_validators import validator


class ForDB(BaseModel):
    """Валидация данных"""

    id_question: int = Field(alias='id')
    question: str
    answer: str
    created_at: datetime

    @validator('question')
    def valid_question(cls, value: str):
        return sub('[\"|<i>]', "", value)

    @validator('answer')
    def valid_answer(cls, value: str):
        return sub('[\"|<i>]', "", value)
