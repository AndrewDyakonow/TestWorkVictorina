from sqlalchemy.orm import mapped_column, Mapped, registry
from datetime import datetime

mapper_registry = registry()
Base = mapper_registry.generate_base()


class VictorinaModel(Base):
    """Модель таблицы в БД"""
    __tablename__ = "questions"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    id_question: Mapped[int] = mapped_column(unique=True)
    question: Mapped[str]
    answer: Mapped[str]
    created_at: Mapped[datetime]

    def __str__(self):
        return f"{self.id}, {self.id_question}, {self.question}, {self.answer}"
