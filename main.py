from flask import Flask, request
import telebot
import os

TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("📘 Get Course", "🔍 Understand First")
    markup.row("💳 Pay Now", "✅ I Paid")
    bot.send_message(message.chat.id, "Welcome to RENI AI Helper Bot. What would you like to do?", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def handle_buttons(message):
    if message.text == "📘 Get Course":
        bot.send_message(message.chat.id, "Please go to https://yourcourse.link to access the course.")
    elif message.text == "🔍 Understand First":
        bot.send_message(message.chat.id, "This bot helps you understand how to use RENI System.")
    elif message.text == "💳 Pay Now":
        bot.send_message(message.chat.id, "You can pay via https://yourpayment.link")
    elif message.text == "✅ I Paid":
        bot.send_message(message.chat.id, "Thank you! We are verifying your payment.")
    else:
        bot.send_message(message.chat.id, "Please choose an option from the keyboard.")

@server.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@server.route("/")
def index():
    return "RENI Telegram Bot is running!"

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
