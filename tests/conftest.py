import asyncio

import pytest

from httpx import AsyncClient
from main import app, get_db
from tests.test_dealer import TestingSessionLocal, engine, Base

@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture(scope="session")
async def test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


# Фикстура для клиента
@pytest.fixture
async def client(test_db):
    async def override_get_db():
        async with TestingSessionLocal() as session:
            yield session
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
async def new_dealer(client):
    response = await client.post("/api/v1/dealer", json={"name": "john johnes"})
    assert response.status_code == 200
    return response.json()

@pytest.fixture
async def new_order(client):
    response = await client.post("/api/v1/order", json={"dealer_id":1})
    assert response.status_code == 200
    return response.json()


