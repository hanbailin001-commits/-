from .database import SessionLocal
from . import models
import json

def create_user_if_not_exists(telegram_user: dict):
    db = SessionLocal()
    tg_id = str(telegram_user.get('id'))
    user = db.query(models.User).filter(models.User.telegram_id==tg_id).first()
    if not user:
        user = models.User(telegram_id=tg_id, username=telegram_user.get('username'), display_name=telegram_user.get('first_name'))
        db.add(user)
        db.commit()
        db.refresh(user)
    db.close()
    return user

def create_message(payload: dict):
    db = SessionLocal()
    msg = models.Message(payload=payload)
    db.add(msg)
    db.commit()
    db.refresh(msg)
    db.close()
    return msg
