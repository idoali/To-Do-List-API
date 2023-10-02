from fastapi import Depends, FastAPI, HTTPException, status, APIRouter 
from sqlalchemy.orm import Session 
from .. import crud, models, schemas, utils, oauth2
from ..database import engine, get_db 
from fastapi.security.oauth2 import OAuth2PasswordRequestForm 

router = APIRouter(
    prefix = "/todos",
    tags = ["doing"]
)

        
@router.post("/", response_model = schemas.ItemBase)
def create_todo(act: schemas.ItemBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    doing_past = db.query(models.Doings).filter(models.Doings.title == act.title).first()
    # print(len(doing.title))
    if doing_past:
        raise HTTPException(status_code = 404,
                            detail = "That activity already exist")
    
    db_doing = models.Doings(title = act.title, description = act.description, user_id = current_user)
    db.add(db_doing)
    db.commit()
    db.refresh(db_doing)
    
    return db_doing

@router.get("/", response_model = list[schemas.ItemFull])
def get_all_doings(db: Session = Depends(get_db)):
    db_doing = db.query(models.Doings).all()
    return db_doing 

@router.get("/{doing_id}", response_model = schemas.ItemFull)
def get_doing(doing_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    doing_query = db.query(models.Doings).filter(models.Doings.id == doing_id, models.Doings.user_id == current_user)
    
    if doing_query == None:
        raise HTTPException(status_code = 404,
                            detail = "The activity is illegal. User and Item doesn't match")
    
    doing = doing_query.first()
    return doing 

@router.put("/{doing_id}", response_model = schemas.ItemBase)
def edit_doing(doing_id: int, updated_post: schemas.ItemBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    doing_query = db.query(models.Doings).filter(models.Doings.id == doing_id, models.Doings.user_id == current_user)
    post = doing_query.first()
    
    if post == None:
        raise HTTPException(status_code = 404,
                            detail = f"post with id: {id} does not exist")
    
    doing_query.update(updated_post.dict(), synchronize_session = False)
    db.commit()
    db_output = doing_query.first()
    return db_output 

@router.delete("/{doing_id}")
def delete_doing(doing_id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    doing_query = db.query(models.Doings).filter(models.Doings.id == doing_id, models.Doings.user_id == current_user)
    the_doing = doing_query.first()
    
    if the_doing == None:
        raise HTTPException(status_code = 404,
                            detail = f"post with id: {doing_id} doesn't exist in the first place")
    doing_query.delete(synchronize_session = False)
    db.commit()
    
    return {"Status": "Deleted Successful"}