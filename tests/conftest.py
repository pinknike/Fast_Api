import os
import sys

import pytest
from httpx import AsyncClient
from main import app, get_db
from tests.test_crud import TestingSessionLocal, engine, Base

@pytest.fixture(scope="function")
async def test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield TestingSessionLocal
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
@pytest.fixture(scope="function")
async def client(test_db):
    async def override_get_db():
        async with TestingSessionLocal() as session:
            yield session
    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def new_dealer(client):
    response = await client.post("/api/v1/dealer", json={"name": "john johnes"})
    assert response.status_code == 200
    return response.json()

@pytest.fixture(scope="function")
async def session(test_db):
    async with test_db() as session:
        yield session