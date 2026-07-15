from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import hmac
import hashlib
import os
import time
import jwt

SECRET_KEY = os.getenv('JWT_SECRET','devsecret')

app = FastAPI()

class WebAppLoginIn(BaseModel):
    init_data: str

# Simplified auth functions for demonstration

def verify_telegram_init(init_data: str):
    # Expect init_data as query-string-like 'id=...&auth_date=...&hash=...'
    try:
        parts = dict([p.split('=') for p in init_data.split('&')])
        hash_val = parts.pop('hash')
        # Recreate hash with bot token
        bot_token = os.getenv('BOT_TOKEN','')
        data_check = '\n'.join([f"{k}={v}" for k,v in sorted(parts.items())])
        secret = hashlib.sha256(bot_token.encode()).digest()
        calc = hmac.new(secret, data_check.encode(), hashlib.sha256).hexdigest()
        if calc != hash_val:
            return None
        # Check auth_date freshness
        if abs(time.time() - int(parts.get('auth_date',0))) > 86400:
            return None
        return parts
    except Exception:
        return None


def create_jwt_for_user(user_id: str):
    payload = {'sub': user_id, 'iat': int(time.time()), 'exp': int(time.time()) + 3600}
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')


def get_current_user(token: str = Depends()):
    # For simplicity we accept token as query param (not ideal)
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return data
    except Exception:
        raise HTTPException(status_code=401, detail='invalid token')
