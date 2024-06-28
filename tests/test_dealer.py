import asyncio
import logging

import pytest

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base



SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(expire_on_commit=False,autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@pytest.mark.asyncio
async def test_create_dealer(client,test_db):
    response = await client.post("/api/v1/dealer", json={"name": "john johnes"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "john johnes"
    assert "id" in data


@pytest.mark.asyncio
async def test_read_dealer(client, test_db,new_dealer):
    dealer_id = new_dealer["id"]
    response = await client.get(f"/api/v1/dealer/{dealer_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "john johnes"
    assert data["id"] == dealer_id

@pytest.mark.asyncio
async  def test_read_all(client,test_db,new_dealer):
    responce = await client.get("/api/v1/dealers")
    assert responce.status_code == 200
    data = responce.json()
    assert len(data)>0

@pytest.mark.asyncio
async def test_delete_dealer(client,test_db,new_dealer):
    dealer_id = new_dealer["id"]
    responce = await client.get(f"/api/v1/dealer/{dealer_id}")
    assert responce.status_code == 200

    responce = await client.delete(f"/api/v1/dealer/{dealer_id}")
    assert responce.status_code == 200

    responce = await client.get(f"/api/v1/dealer/{dealer_id}")
    assert responce.status_code == 404



#если запускаю два теста post и get то ошибка!если get и фикстура создания-работает!только post тоже работает!