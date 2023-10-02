from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session 
from . import models, schemas, utils, oauth2 
from database import engine, get_db 
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 
from routers import todo, auth, users 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo.router)
app.include_router(users.router)
app.include_router(auth.router)

# @app.get("/")
# def home():
#     return {"Status": "Successful"}
        
# @app.post("/todos/", response_model = schemas.ItemBase)
# def create_todo(act: schemas.ItemBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     db_doing = crud.create_doing(db, doing = act, user_id = current_user)
#     return db_doing

# @app.get("/todos/", response_model = list[schemas.ItemFull])
# def get_all_doings(db: Session = Depends(get_db)):
#     db_doing = crud.get_all_doings(db)
#     return db_doing 

# @app.get("/todos/{doing_id}", response_model = schemas.ItemFull)
# def get_doing(doing_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     db_doing = crud.get_doing(db = db, id = doing_id, user = current_user)
#     return db_doing 

# @app.put("/todos/{doing_id}", response_model = schemas.ItemBase)
# def edit_doing(doing_id: int, updated_post: schemas.ItemBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     db_doing = crud.update_doing(doing_id = doing_id, db = db, doing = updated_post, current_user= current_user)
#     return db_doing

# @app.delete("/todos/{doing_id}")
# def delete_doing(doing_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
#     status = crud.delete_doing(doing_id = doing_id, db = db, current_user= current_user)
#     return status

# Making Users

# @app.post("/user/", response_model = schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password 
    
#     new_user = models.Users(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get("/user/{id}", response_model = schemas.UserOut)
# def get_user(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.Users).filter(models.Users.id == id).first()
    
#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
#                             detail = f"User with id: {id} does not exist")
    
#     return user 

# # For auth.py 

# @app.post("/login/")
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


    

    

