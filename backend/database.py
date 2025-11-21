from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker


DATABASE_URL = "postgresql+asyncpg://maruf:maruf18009@localhost:5432/todo_list"

engine = create_async_engine(DATABASE_URL,echo=True)

SessionLocal = async_sessionmaker(bind=engine,expire_on_commit=False)

