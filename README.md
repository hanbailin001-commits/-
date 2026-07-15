# Telegram Bot + WebApp skeleton

## Overview
This repository contains a starter skeleton for a Telegram bot backend (FastAPI) and a Telegram WebApp (React + Vite).

### What I pushed
- backend/: FastAPI app with webhook endpoint and basic auth skeleton
- web/: React + Vite minimal WebApp that demonstrates sending Telegram init_data to the backend
- docker-compose.yml, .env.example, README

## Local development (recommended flow)
1. Create a Telegram bot via BotFather and obtain BOT_TOKEN. **DO NOT** paste tokens into public places.
2. Revoke any tokens you leaked earlier and generate a new one.
3. Add a GitHub Secret named `SECRET_BOT_TOKEN` with your BOT token (if using GitHub Actions) or put it into `.env` for local dev.
4. Start the services:
   - For quick local dev you can run the backend directly:
     ```
     cd backend
     python -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt
     uvicorn app.main:app --reload --port 8000
     ```

5. Use ngrok to expose your local backend for Telegram webhook testing:
   ngrok http 8000
   Then set webhook:
   curl -X POST "https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook" -d "url=https://<your-ngrok>/webhook/telegram"

## Notes
- This is a skeleton. You should rotate secrets, configure production Postgres, TLS, and extend auth, DB models, and admin UI for production use.
