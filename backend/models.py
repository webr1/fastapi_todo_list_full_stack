from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import String, Boolean, Integer


class Base(DeclarativeBase):
    pass


"""  MODEL TODO_LIST  """
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True,index=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500),nullable=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)


