# Room Reservation

## Cтек технологий:
[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=56C0C0&color=008080)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/-FastAPI-464646?style=flat&logo=fastapi&logoColor=56C0C0&color=008080)](https://fastapi.tiangolo.com/)
[![uvicorn](https://img.shields.io/badge/-Uvicorn-464646?style=flat&logo=uvicorn&logoColor=56C0C0&color=008080)](https://www.uvicorn.org/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=sqlalchemy&logoColor=56C0C0&color=008080)](https://www.sqlalchemy.org/)

## Установка
1. Клонируйте репозиторий:
```
git clone git@github.com:igredk/room_reservation.git
```
2. Активируйте виртуальное окружение:
```
$ poetry shell
```
3. Установите зависимости:
```
$ poetry install
```
4. Создайте в корневой директории файл .env со следующим наполнением:
```
APP_TITLE=Сервис бронирования переговорных комнат
APP_DESCRIPTION=Приложение предоставляет возможность бронировать помещения на определённый период времени.
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=reallyweirdsecretkey
FIRST_SUPERUSER_EMAIL=jon@example.com
FIRST_SUPERUSER_PASSWORD=jonhopkins
FIRST_SUPERUSER_NAME=Jon
FIRST_SUPERUSER_LAST_NAME=Hopkins
```
5. Примените миграции для создания базы данных:
```
$ alembic upgrade head
```
6. Для запуска проекта выполните команду:
```
uvicorn app.main:app
```
Интерактивная документация Swagger доступна по адресу:
```
http://localhost:8000/docs
```

## Лицензия
- ### **MIT License**

### Автор
Igor Redkin

igredk@gmail.com