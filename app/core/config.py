from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = "Бронирование переговорок"
    app_description: str = "Бронирование переговорок на время"
    database_url: str
    secret: str
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    first_superuser_name: Optional[str] = None
    first_superuser_last_name: Optional[str] = None

    class Config:
        env_file = ".env"


settings = Settings()
