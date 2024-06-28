from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Dealer(Base):
    __tablename__ = "Dealer"
    id = Column(Integer,primary_key=True)
    name = Column(String)

class Order(Base):
    __tablename__="Order"
    id = Column(Integer, primary_key=True)
    dealer_id = Column(Integer,ForeignKey("Dealer.id"))
    dealer = relationship("Dealer")