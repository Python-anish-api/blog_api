from sqlalchemy.orm.session import Session
from fastapi import HTTPException, status
from  routers.schemas import PostBase
from .models import DbPost
import datetime
def create(request: PostBase, db: Session):
    new_post = DbPost(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now()

    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    


def get_all(db:Session):
    all_posts = db.query(DbPost).all()    
    return all_posts


def delete_post(id: int, db:Session):
    post = db.query(DbPost).filter(DbPost.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id {id} not found')
    
    db.delete(post)
    db.commit()
    


