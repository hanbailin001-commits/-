# Additional auth endpoint: /webapp_login

Example POST request (JSON):

{
  "init_data": "id=12345&auth_date=1650000000&hash=abcdef..."
}

Example successful response:

{
  "token": "<JWT>"
}

Server uses SECRET_BOT_TOKEN (repo secret) to rebuild and verify the hash, then returns a JWT signed with JWT_SECRET.
