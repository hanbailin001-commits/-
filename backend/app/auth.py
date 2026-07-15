import os
import hmac, hashlib
from urllib.parse import parse_qs
import base64
import json
import jwt

BOT_TOKEN = os.getenv('BOT_TOKEN','')
JWT_SECRET = os.getenv('JWT_SECRET','changeme')

def _parse_init_data(init_data: str) -> dict:
    # init_data is like "key1=value1&key2=value2"
    qs = parse_qs(init_data, keep_blank_values=True)
    # simplify
    return {k: v[0] for k,v in qs.items()}

def verify_telegram_init(init_data: str) -> dict|None:
    # Verify according to Telegram docs
    data = _parse_init_data(init_data)
    hash_in = data.get('hash')
    if not hash_in:
        return None
    data_check_arr = []
    for k in sorted([k for k in data.keys() if k!='hash']):
        data_check_arr.append(f"{k}={data[k]}")
    data_check_string = "\n".join(data_check_arr)
    secret_key = hashlib.sha256(BOT_TOKEN.encode()).digest()
    hmac_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
    if hmac_hash != hash_in:
        return None
    # return basic user info
    return {
        'id': data.get('id'),
        'first_name': data.get('first_name'),
        'username': data.get('username')
    }

def create_jwt_for_user(user_id: str) -> str:
    payload = {"sub": user_id}
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')
    return token

from fastapi import Depends, HTTPException

def get_current_user(token: str):
    # Very minimal: token is JWT itself
    try:
        data = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
        return {"user_id": data.get('sub')}
    except Exception as e:
        raise HTTPException(status_code=401, detail='invalid token')
