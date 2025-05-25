# RENI Telegram Bot (English Version)

## Deployment Instructions:

1. Upload all files to a new GitHub repository.
2. Connect the repository to Render.com as a Web Service.
3. Set the Build Command to:
   pip install -r requirements.txt
4. Set the Start Command to:
   gunicorn main:server
5. Add an environment variable:
   API_TOKEN=your_telegram_bot_token
6. Click "Deploy".

Bot will be accessible at the Render-generated URL.
