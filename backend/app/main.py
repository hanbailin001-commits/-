from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
import os
from .database import SessionLocal, engine, Base
from . import models, crud, auth
from pydantic import BaseModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Telegram Bot Backend")

class WebAppLoginIn(BaseModel):
    init_data: str

@app.post('/webhook/telegram')
async def telegram_webhook(request: Request):
    update = await request.json()
    # Minimal handling: persist update and respond
    try:
        crud.create_message(update)
    except Exception as e:
        print('db error', e)
    return JSONResponse({"ok": True})

@app.post('/api/auth/webapp-login')
async def webapp_login(payload: WebAppLoginIn):
    # Verify init_data and issue JWT
    user = auth.verify_telegram_init(payload.init_data)
    if not user:
        raise HTTPException(status_code=400, detail='invalid init_data')
    token = auth.create_jwt_for_user(user['id'])
    return {"access_token": token}

@app.get('/api/user/me')
async def me(token: str = Depends(auth.get_current_user)):
    return token
