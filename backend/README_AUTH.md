# Backend Auth README

This file describes the simple auth helpers included for WebApp login and JWT issuance.

## Environment variables
- `SECRET_BOT_TOKEN` — Telegram bot token (use repository secret name `SECRET_BOT_TOKEN`)
- `JWT_SECRET` — secret used to sign JWTs (set this in `.env` or Secrets)

## WebApp login flow (overview)
1. The WebApp provides `init_data` (query-string-like) which includes `hash` and `auth_date`.
2. Server must verify the `hash` HMAC using `sha256` of your bot token as the secret (see backend/app/auth.py).
3. On success, create a JWT for the corresponding user and return it to the WebApp.

## Example JWT usage
After obtaining a JWT from the server, include it on API requests:

Authorization: Bearer <JWT>

The `create_jwt_for_user(user_id)` helper issues a token valid for 1 hour by default.

## Endpoints (example)
- POST `/webapp_login` — body: { "init_data": "..." } → verifies init_data and returns `{ "token": "<JWT>" }` on success.
- Protected endpoints should require the JWT via `Authorization` header.

