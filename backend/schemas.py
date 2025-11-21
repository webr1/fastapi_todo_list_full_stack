from pydantic import BaseModel
from typing import Optional


class TasksSchema(BaseModel):
    title:str
    description: Optional[str] = None


class TasksCreate(TasksSchema):
    pass

class TasksUpdate(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    is_completed:Optional[bool]=None

class TasksRead(TasksSchema):
    id:int
    is_completed:bool