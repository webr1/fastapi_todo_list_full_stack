from pydantic import BaseModel
from typing import Optional

"""
TasksSchema — базовая структура данных задачи.
Используется как основа для Create и Read схем.
"""
class TasksSchema(BaseModel):
    title: str
    description: Optional[str] = None


"""
TasksCreate — данные, которые приходят от клиента при создании задачи.
Наследует все поля из TasksSchema.
"""
class TasksCreate(TasksSchema):
    pass


"""
TasksUpdate — схема для обновления задачи.
Здесь все поля Optional, чтобы можно было обновлять выборочно.
Например: только title или только is_completed.
"""
class TasksUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None


"""
TasksRead — схема ответа API.
Возвращает данные задачи из базы (включая id и статус).
"""
class TasksRead(TasksSchema):
    id: int
    is_completed: bool
