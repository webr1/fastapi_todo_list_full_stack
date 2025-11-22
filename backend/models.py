from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import String, Boolean, Integer


# Базовый класс для всех моделей SQLAlchemy
class Base(DeclarativeBase):
    pass


""" Модель таблицы задач (TODO List) """
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)  # ID задачи
    title: Mapped[str] = mapped_column(String(100))                # Заголовок
    description: Mapped[str] = mapped_column(String(500), nullable=True)  # Описание (может быть пустым)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)    # Выполнена задача или нет
