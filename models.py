from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship 
from .database import Base 

class Doings(Base):
    __tablename__ = "todo"
    
    id = Column(Integer, primary_key = True)
    title = Column(String, unique = True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
    
class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True)
    password = Column(String)
    
    