from fastapi import APIRouter , Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update ,delete

from backend.dependencies import SessionDep, get_session
from backend.models import Task
from backend.schemas import TasksRead,TasksCreate,TasksSchema,TasksUpdate


router_task = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)



@router_task.get("/tasks_all",response_model=list[TasksRead])
async def get_tasks(session:AsyncSession = Depends(get_session)):
    result = await session.execute(select(Task))
    if result:
        task =result.scalars().all()
        return task
   


@router_task.post("/add_tasks",response_model=TasksRead)
async def create_tasks(
    task:TasksCreate,
    session:AsyncSession = Depends(get_session)
    ):
    new_task = Task(
        title=task.title,
        description=task.description,
    )
    session.add(new_task)
    await session.commit()
    await session.refresh(new_task)
    return new_task



@router_task.put("/update/{task_id}",response_model=TasksUpdate)
async def update_tasks(
    task_id:int,
    task:TasksUpdate,
    session:AsyncSession = Depends(get_session),
    ):
    qwery =  select(Task).where(Task.id ==task_id)
    result = await session.execute(qwery)
    db_task= result.scalar_one_or_none()

    if not db_task:
        raise HTTPException(404,"Task not found")
    if task.title is not None:
        db_task.title = task.title
    if task.description is not None:
        db_task.description = task.description
    if task.is_completed is not None:
        db_task.is_completed = task.is_completed

    await session.commit()
    await session.refresh(db_task)
    return db_task


@router_task.delete("/delete/{task_id}")
async def delete_tasks(task_id:int,
                       session:AsyncSession = Depends(get_session)):
    qwery = select(Task).where(Task.id == task_id)
    result =  await session.execute(qwery)
    db_task = result.scalar_one_or_none()
    
    if not db_task:
        raise HTTPException(
            404,"Task ot found"
        )


    await session.delete(db_task)
    await session.commit()
    return {
        "message":"Task has been deleted already",
        "status":200
    }