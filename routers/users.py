from fastapi import Depends, FastAPI, HTTPException, status, APIRouter 
from sqlalchemy.orm import Session 
from .. import crud, models, schemas, utils, oauth2
from ..database import engine, get_db 
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 

router = APIRouter(
    prefix = "/user",
    tags = ["user"]
)

@router.post("/user/", response_model = schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password 
    
    new_user = models.Users(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/user/{id}", response_model = schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.Users).filter(models.Users.id == id).first()
    
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"User with id: {id} does not exist")
    
    return user 

# For auth.py 

# @router.post("/login/")
# def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(models.Users).filter(models.Users.name == user_credentials.username).first()
#     if not user:
#         raise HTTPException(
#             status_code = status.HTTP_403_FORBIDDEN, detail = f"Invalid Credentials"
#         )
#     if not utils.verify(user_credentials.password, user.password):
#         raise HTTPException(
#             status_code = status.HTTP_403_FORBIDDEN, detail = "Invalid Credentials"
#         )
        
#     access_token = oauth2.create_access_token(data = {"user_id": user.id})
#     return {"access_token": access_token, "token_type": "bearer"}