---
title: "Add detailed run & secret configuration and auth endpoints"
---

This PR expands documentation and backend auth helpers to make local testing and CI safer and easier.

What I changed
- Added docs/SECRETS_AND_WEBHOOK.md with step-by-step instructions for storing the bot token in GitHub Secrets and setting the webhook (ngrok + curl examples).
- Added backend/README_AUTH.md describing the WebApp init_data verification flow, JWT usage, and example endpoints.
- Implemented backend auth helpers in backend/app/auth.py (verify_telegram_init, create_jwt_for_user, get_current_user).
- Added README.md and small placeholder files to force a diff for the initial PR.

How to test locally
1. Add your bot token as an environment variable or GitHub secret: SECRET_BOT_TOKEN
2. Run the backend: uvicorn backend.app.main:app --reload --port 8000
3. Start ngrok: ngrok http 8000 and set your webhook using the curl example in docs/SECRETS_AND_WEBHOOK.md

Security notes
- Never commit your bot token. Use GitHub Secrets for CI and environment variables for local runs.
- Rotate tokens in BotFather if a token is exposed.

Next steps
- Harden WebApp init_data validation with edge-case tests.
- Add CI workflow and minimal tests.
- Implement bot handlers and webhook processing.
