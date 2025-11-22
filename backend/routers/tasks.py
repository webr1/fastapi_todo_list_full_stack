from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.dependencies import get_session
from backend.models import Task
from backend.schemas import TasksRead, TasksCreate, TasksUpdate


# Роутер для всех операций с задачами
router_task = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


# =======================
#        GET ALL TASKS
# =======================
@router_task.get("/tasks_all", response_model=list[TasksRead])
async def get_tasks(session: AsyncSession = Depends(get_session)):
    """
    Получить список всех задач.

    - Выполняет SELECT * FROM tasks
    - Возвращает список объектов Task
    - Использует scalars().all(), чтобы получить ORM-объекты
    """
    result = await session.execute(select(Task))
    tasks = result.scalars().all()
    return tasks


# =======================
#        CREATE TASK
# =======================
@router_task.post("/add_tasks", response_model=TasksRead)
async def create_tasks(
    task: TasksCreate,
    session: AsyncSession = Depends(get_session)
):
    """
    Создание новой задачи.

    - Получает данные от клиента (title, description)
    - Создает объект Task
    - Добавляет его в базу
    - Возвращает созданную задачу
    """
    new_task = Task(
        title=task.title,
        description=task.description,
    )

    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)

    return new_task


# =======================
#        UPDATE TASK
# =======================
@router_task.put("/update/{task_id}", response_model=TasksUpdate)
async def update_tasks(
    task_id: int,
    task: TasksUpdate,
    session: AsyncSession = Depends(get_session),
):
    """
    Обновление задачи по ID.

    - Выполняет SELECT задачи
    - Если задача не найдена → 404
    - Обновляет только те поля, которые пользователь отправил
    - Сохраняет изменения в базе
    """

    query = select(Task).where(Task.id == task_id)
    result = await session.execute(query)
    db_task = result.scalar_one_or_none()

    if not db_task:
        raise HTTPException(404, "Task not found")

    # Обновляем только не-None значения
    if task.title is not None:
        db_task.title = task.title
    if task.description is not None:
        db_task.description = task.description
    if task.is_completed is not None:
        db_task.is_completed = task.is_completed

    await session.commit()
    await session.refresh(db_task)

    return db_task


# =======================
#        DELETE TASK
# =======================
@router_task.delete("/delete/{task_id}")
async def delete_tasks(
    task_id: int,
    session: AsyncSession = Depends(get_session)
):
    """
    Удаление задачи по ID.

    - Ищет задачу в базе
    - Если нет → 404
    - Удаляет задачу
    - Возвращает сообщение об успехе
    """

    query = select(Task).where(Task.id == task_id)
    result = await session.execute(query)
    db_task = result.scalar_one_or_none()

    if not db_task:
        raise HTTPException(404, "Task not found")

    await session.delete(db_task)
    await session.commit()

    return {
        "message": "Task has been deleted successfully",
        "status": 200
    }
