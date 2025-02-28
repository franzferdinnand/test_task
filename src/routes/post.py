from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.controller.post import add_post, get_posts, delete_post
from src.controller.auth import verify_token
from src.schemas.post import PostCreate
from src.db import get_db

router = APIRouter()

@router.post("/addPost")
def create_post(post: PostCreate, token: str, db: Session = Depends(get_db)):
    user_id = verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    return add_post(db, user_id, post.text)

@router.get("/getPosts")
def fetch_posts(token: str, db: Session = Depends(get_db)):
    user_id = verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    return get_posts(db, user_id)

@router.delete("/deletePost/{post_id}")
def remove_post(post_id: int, token: str, db: Session = Depends(get_db)):
    user_id = verify_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    return delete_post(db, user_id, post_id)