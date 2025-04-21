from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def add_points(db: Session, user_id: int, points: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.points += points
        db.commit()
        db.refresh(db_user)
    return db_user
