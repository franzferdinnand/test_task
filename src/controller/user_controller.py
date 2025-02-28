from sqlalchemy.orm import Session

from src.schemas.user import UserCreate
from src.models.users import User


def users_list(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user_data: UserCreate):
    user = User(first_name=user_data.first_name, email=user_data.email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user

def update_user(db: Session, user_data: UserCreate, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    user.first_name = user_data.first_name
    user.last_name = user_data.last_name
    user.email = user_data.email
    db.commit()
    db.refresh(user)
    return user
