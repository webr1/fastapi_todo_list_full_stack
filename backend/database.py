from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker

""" Это подключение к безе данных postgresql тут есть port и password и name """
DATABASE_URL = "postgresql+asyncpg://maruf:maruf18009@localhost:5432/todo_list"  

""" Создаём подключение к PostgreSQL (асинхронный движок SQLAlchemy) """
engine = create_async_engine(DATABASE_URL, echo=True)

""" Фабрика для создания асинхронных сессий работы с базой данных """
SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)
