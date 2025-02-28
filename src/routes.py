from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.users import User
from src.controller.user_controller import users_list, create_user
from src.db import get_db
from src.schemas.user import UserCreate, UserResponse

from controller.user_controller import get_user

router = APIRouter()

@router.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return users_list(db)

@router.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email вже використовується")

    return create_user(db, user)
