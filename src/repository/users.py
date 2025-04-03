from sqlalchemy.orm import Session
from src.database.models import User
from src.schemas import UserCreate
from src.services.auth import hash_password


def create_user(db: Session, user_data: UserCreate):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        return None

    hashed_password = hash_password(user_data.password)
    new_user = User(email=user_data.email, hashed_password=hashed_password, is_verified=False)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def verify_user_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if user and not user.is_verified:
        user.is_verified = True
        db.commit()
        db.refresh(user)
    return user
