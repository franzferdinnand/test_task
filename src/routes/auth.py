from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.controller.auth import create_user, authenticate_user, create_token
from src.schemas.user import UserCreate
from src.db import get_db

router = APIRouter()

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.email, user.password)

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user.email, user.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": create_token(user.id)}
