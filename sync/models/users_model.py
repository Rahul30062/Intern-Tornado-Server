
from sqlalchemy.orm import Relationship
from sqlalchemy import String, Integer,Column,Date
from db_init import Base


class User(Base):
    
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user_email = Column(String, nullable=False, unique=True)
    ph_no = Column(String, nullable=False, unique=True)
    user_created = Column(Date)
    
    orders = Relationship ("Order", back_populates = "users")

    
    
    