from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.post import Post
from src.cache import redis_client

def add_post(db: Session, user_id: int, text: str):
    post = Post(text=text, user_id=user_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def get_posts(db: Session, user_id: int):
    cache_key = f"user_posts_{user_id}"
    cached_posts = redis_client.get(cache_key)
    if cached_posts:
        return cached_posts
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    redis_client.setex(cache_key, 300, posts)
    return posts

def delete_post(db: Session, user_id: int, post_id: int):
    post = db.query(Post).filter(Post.id == post_id, Post.user_id == user_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found or unauthorized")

    db.delete(post)
    db.commit()

    # Очищаємо кеш для користувача після видалення поста
    cache_key = f"user_posts_{user_id}"
    redis_client.delete(cache_key)

    return {"message": "Post deleted successfully"}