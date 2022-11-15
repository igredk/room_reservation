import contextlib

from fastapi_users.exceptions import UserAlreadyExists
from pydantic import EmailStr

from app.core.config import settings
from app.core.db import get_async_session
from app.core.user import get_user_db, get_user_manager
from app.schemas.user import UserCreate

# создаем из асинхронных генераторов асинхронные менеджеры контекста
get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(
    email: EmailStr,
    password: str,
    first_name: str,
    last_name: str,
    is_superuser: bool = False,
) -> None:
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    await user_manager.create(
                        UserCreate(
                            email=email,
                            password=password,
                            first_name=first_name,
                            last_name=last_name,
                            is_superuser=is_superuser,
                        )
                    )
    except UserAlreadyExists:
        pass


async def create_first_superuser() -> None:
    if (
        settings.first_superuser_email
        and settings.first_superuser_password
        and settings.first_superuser_name
        and settings.first_superuser_last_name
    ):
        await create_user(
            email=settings.first_superuser_email,
            password=settings.first_superuser_password,
            first_name=settings.first_superuser_name,
            last_name=settings.first_superuser_last_name,
            is_superuser=True,

        )
