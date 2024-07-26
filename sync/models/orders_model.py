
from sqlalchemy import String, Integer,Column,DateTime,Float,Text,ForeignKey
from sqlalchemy.orm import Relationship
from db_init import Base

class Order(Base):
    
    __tablename__ = "Orders"
    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    product_desc = Column(Text, nullable=False, unique=True)
    product_amount = Column(Float, nullable=False) 
    product_ordered = Column(DateTime)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    users = Relationship ("User", back_populates = "orders")
    
    