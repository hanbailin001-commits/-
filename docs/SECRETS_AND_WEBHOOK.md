# Secrets & Webhook Setup

This document explains how to securely store your Telegram Bot token and how to set the bot webhook for local testing (ngrok) and production.

## Repository Secret (recommended)
1. Go to your repository on GitHub: https://github.com/hanbailin001-commits/-
2. Click `Settings` → `Secrets and variables` → `Actions` → `New repository secret`.
3. Add a secret with:
   - Name: `SECRET_BOT_TOKEN`
   - Value: your bot token from BotFather (keep this private — do NOT paste the token in chat)
4. Click `Add secret`.

In GitHub Actions you can reference this as `${{ secrets.SECRET_BOT_TOKEN }}`.

## Environment variables (local)
Set the following in your `.env` or environment when running locally:

- `SECRET_BOT_TOKEN` — your Telegram bot token
- `JWT_SECRET` — a random secret used to sign JWTs (default used only for development)

Example `.env`:

SECRET_BOT_TOKEN="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
JWT_SECRET="replace-with-random-string"

## Using ngrok for local webhook testing
1. Install ngrok and authenticate (https://ngrok.com)
2. Start your local server (default FastAPI port 8000): `uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000`
3. Run: `ngrok http 8000` — you'll get a public HTTPS URL like `https://abcd-1234.ngrok.io`
4. Set the Telegram webhook to point to your public URL + webhook path. Example (see below).

## Setting webhook (curl example)
Replace `<YOUR_TOKEN>` and `<PUBLIC_URL>` appropriately. Prefer using the repository secret where possible.

curl -X POST "https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook" \
  -F "url=<PUBLIC_URL>/webhook"

If using an environment variable in a shell (local):

export TOKEN="$SECRET_BOT_TOKEN"
curl -X POST "https://api.telegram.org/bot$TOKEN/setWebhook" -F "url=https://abcd-1234.ngrok.io/webhook"

If your server requires a trusted certificate, include `-F "certificate=@/path/to/cert.pem"`.

## Notes & Security
- Never commit your bot token to the repository. Use GitHub Secrets for CI and environment variables locally.
- Rotate your token in BotFather if it was accidentally exposed.

