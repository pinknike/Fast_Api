"""Ваша компания занимается продажей оборудования, она принимает заказы от дилеров и по их запросу
(в запрос включены артикулы товаров и их кол-во) делает запрос поставщикам-изготовителям оборудования. 
Задача: с помощью Fast Api и Sql Alchemy придумайте и напишите «сервис» который бы закрывал потребности этой компании, в плане - общения с диллероми и поставщиками.
Необходимо реализовать минимум необходимых моделей и ендпоинтов, чтобы по вашему мнению эта реализация работала"""

from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession
from database import async_session_maker
from routers import dealer, order
app = FastAPI()


# async def get_session() -> AsyncSession:
#     async with async_session_maker() as session:
#         yield session

app.include_router(dealer.router, prefix="/api/v1")
app.include_router(order.router, prefix="/api/v1")


def get_db():
    return None