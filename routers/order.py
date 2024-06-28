from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud import create_order, get_order, order_delete, get_dealer
from dependes import get_session
from schemas import Order as OrderSchema, OrderCreate

router = APIRouter()
@router.post("/order", response_model=OrderSchema)
async def create_order_endpoint(order: OrderCreate, session: AsyncSession = Depends(get_session)):
    return await create_order(session, order)

@router.get("/order/{order_id}", response_model=OrderSchema)
async def get_order_endpoint(order_id: int, session: AsyncSession = Depends(get_session)):
    order = await get_order(order_id, session)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.get("/orders", response_model=list[OrderSchema])
async def get_orders_endpoint(session: AsyncSession = Depends(get_session)):
    return await get_dealer()
    (session)

@router.delete("/order/{order_id}", response_model=OrderSchema)
async def delete_order_endpoint(order_id: int, session: AsyncSession = Depends(get_session)):
    order = await get_order(order_id, session)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    await order_delete(order_id, session)
    return order
