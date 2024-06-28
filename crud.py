from sqlalchemy.ext.asyncio import AsyncSession
from models import Order, Dealer
from schemas import DealerCreate, OrderCreate
from sqlalchemy.future import select

async def Create_Dealer(db: AsyncSession, dealer: DealerCreate):
    new_dealer = Dealer(name=dealer.name)
    db.add(new_dealer)
    await db.commit()
    await db.refresh(new_dealer)
    return new_dealer

async def get_dealer(dealer_id: int, db: AsyncSession):
    result = await db.execute(select(Dealer).where(Dealer.id == dealer_id))
    return result.scalar_one_or_none()

async def get_dealers(db: AsyncSession):
    result = await db.execute(select(Dealer))
    return result.scalars().all()

async def delete_dealer(dealer_id: int, db: AsyncSession):
    dealer = await get_dealer(dealer_id, db)
    if dealer:
        await db.delete(dealer)
        await db.commit()
    return dealer

async def create_order(db: AsyncSession, order: OrderCreate):
    new_order = Order(dealer_id=order.dealer_id)
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    return new_order

async def get_order(order_id: int, db: AsyncSession):
    result = await db.execute(select(Order).where(Order.id == order_id))
    return result.scalar_one_or_none()

async def get_orders(db: AsyncSession):
    result = await db.execute(select(Order))
    return result.scalars().all()

async def order_delete(order_id: int, db: AsyncSession):
    order = await get_order(order_id, db)
    if order:
        await db.delete(order)
        await db.commit()
    return order
