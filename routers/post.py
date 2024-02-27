from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from database.database import get_db
from database import db_post
from routers.schemas import PostBase


router = APIRouter(prefix='/post',tags=['POST'])

@router.post('',)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db=db, request=request)



@router.get('/all-posts')
def all_posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)