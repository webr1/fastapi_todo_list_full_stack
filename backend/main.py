from backend.database import engine
from backend.routers.tasks import router_task
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from fastapi import FastAPI
import uvicorn


app = FastAPI()


# Разрешённые источники (фронт)
origins = [
    "http://127.0.0.1:5500",    # если открываешь через Live Server
    "http://localhost:5500",
    "http://127.0.0.1:3000",    # если когда-нибудь будет React
    "http://localhost:3000",
    "http://127.0.0.1",         # если открываешь index.html напрямую
    "http://localhost",
    "*"                         # разрешить все домены (для разработки)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # откуда можно приходить
    allow_credentials=True,
    allow_methods=["*"],           # разрешить GET, POST, DELETE, PUT
    allow_headers=["*"],           # разрешить все заголовки
)


app.include_router(router_task)

@app.get("/check_db")
async def check_db():
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        return {
            "status":"conected"
        }
    except Exception as e:
        return {
            "error":str(e)
        }





