from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm.session import Session
from database.database import get_db
from database import db_post
from routers.schemas import PostBase
import string, shutil, random

router = APIRouter(prefix='/post',tags=['POST'])

@router.post('',)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db=db, request=request)



@router.get('/all-posts')
def all_posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)


@router.delete('/delete-post/{id}')
def delete_post(id: int , db: Session = Depends(get_db)):
    return db_post.delete_post(id=id, db=db)


@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letter = string.ascii_letters
    random_string = ''.join(random.choice(letter) for i in range(4))   
    new  = f'_{random_string}'
    filename = new.join(image.filename.rsplit(".", 1))
    path = f'images/{filename}'
    
    
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
        
    return {
        'filename': path,
    }    
    