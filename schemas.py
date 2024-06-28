from pydantic import BaseModel

class DealerCreate(BaseModel):
    name: str

class Dealer(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    dealer_id: int

class Order(BaseModel):
    id: int
    dealer_id : int

    class Config:
        from_attributes = True