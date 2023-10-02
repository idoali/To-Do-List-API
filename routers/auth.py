from fastapi import Depends, FastAPI, HTTPException, status, APIRouter 
from sqlalchemy.orm import Session 
from .. import crud, models, schemas, utils, oauth2
from ..database import engine, get_db 
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 

router = APIRouter(
    prefix = "/login",
    tags = ["user"]
)

# For auth.py 

@router.post("/login/")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.name == user_credentials.username).first()
    if not user:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials"
        )
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN, detail = "Invalid Credentials"
        )
        
    access_token = oauth2.create_access_token(data = {"user_id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}