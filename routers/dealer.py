from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud import Create_Dealer, get_dealer, get_dealers, delete_dealer
from dependes import get_session
from database import init_db
from schemas import Dealer as DealerSchema, DealerCreate

router = APIRouter()
@router.on_event("startup")
async def on_startup():
    await init_db()

@router.post("/dealer", response_model=DealerSchema)
async def create_dealer_endpoint(dealer: DealerCreate, session: AsyncSession = Depends(get_session)):
    return await Create_Dealer(session, dealer)

@router.get("/dealer/{dealer_id}", response_model=DealerSchema)
async def get_dealer_endpoint(dealer_id: int, session: AsyncSession = Depends(get_session)):
    dealer = await get_dealer(dealer_id, session)
    if dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")
    return dealer

@router.get("/dealers", response_model=list[DealerSchema])
async def get_dealers_endpoint(session: AsyncSession = Depends(get_session)):
    return await get_dealers(session)

@router.delete("/dealer/{dealer_id}", response_model=DealerSchema)
async def delete_dialers_endpoint(dealer_id: int, session: AsyncSession = Depends(get_session)):
    dealer = await get_dealer(dealer_id, session)
    if dealer is None:
        raise HTTPException(status_code=404, detail="Dealer not found")
    await delete_dealer(dealer_id, session)
    return dealer
