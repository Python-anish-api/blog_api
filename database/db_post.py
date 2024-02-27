from sqlalchemy.orm.session import Session
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