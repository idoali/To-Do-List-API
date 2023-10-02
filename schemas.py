from pydantic import BaseModel 
from datetime import datetime 

class ItemBase(BaseModel):
    title: str 
    description: str | None = None 

class ItemFull(ItemBase):
    id: int
    user_id: int   
    
class UserOut(BaseModel):
    name: str 
    password: str 
    
class Users(UserOut):
    id: int 
    
class UserCreate(BaseModel):
    name: str 
    password: str 
    
class TokenData(BaseModel):
    id: int 