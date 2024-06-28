
import pytest

@pytest.mark.asyncio
async def test_create_order(client,test_db,):
    responce = await client.post("/api/v1/order",json={"dealer_id":1})
    assert responce.status_code == 200
    data = responce.json()
    assert data["dealer_id"]==1


@pytest.mark.asyncio
async def test_read_order(client, test_db,new_order):
    order_id = new_order["id"]
    response = await client.get(f"/api/v1/dealer/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id

@pytest.mark.asyncio
async def test_read_all_orders(client, test_db):
    response = await client.get(f"/api/v1/orders")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

@pytest.mark.asyncio
async def test_delete_order(client, test_db,new_order):
    order_id = new_order["id"]
    responce = await client.get(f"/api/v1/order/{order_id}")
    assert responce.status_code == 200

    responce = await client.delete(f"/api/v1/order/{order_id}")
    assert responce.status_code == 200

    responce = await client.get(f"/api/v1/order/{order_id}")
    assert responce.status_code == 404







