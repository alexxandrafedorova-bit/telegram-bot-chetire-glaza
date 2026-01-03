import os
from flask import Flask, request
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# --- КНОПКИ ---
def main_keyboard():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    kb.add(
        KeyboardButton("🛒 Оформить заказ", web_app=WebAppInfo(url="https://4glaza-72.ru"))
    )

    kb.add(
        KeyboardButton("📞 Позвонить"),
        KeyboardButton("💬 Связаться с менеджером")
    )

    kb.add(
        KeyboardButton("📍 Адрес"),
        KeyboardButton("⏰ Время работы")
    )

    return kb


# --- СТАРТ ---
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Здравствуйте! 👋\n\n"
        "Добро пожаловать в магазин «Четыре глаза» 🔭\n\n"
        "Нажмите «Оформить заказ», чтобы открыть каталог.",
        reply_markup=main_keyboard()
    )


# --- КНОПКИ ---
@bot.message_handler(func=lambda m: True)
def buttons(message):
    if message.text == "📞 Позвонить":
        bot.send_message(message.chat.id, "📞 +7 922 001 3072")

    elif message.text == "💬 Связаться с менеджером":
        bot.send_message(
            message.chat.id,
            "💬 Написать менеджеру:\nhttps://t.me/Four_eyes72"
        )

    elif message.text == "📍 Адрес":
        bot.send_message(
            message.chat.id,
            "📍 г. Тюмень, ул. 50 лет Октября, 29"
        )

    elif message.text == "⏰ Время работы":
        bot.send_message(
            message.chat.id,
            "⏰ С 10:00 до 20:00 ежедневно"
        )


# --- WEBHOOK ---
@app.route("/webhook", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(
        request.get_data().decode("utf-8")
    )
    bot.process_new_updates([update])
    return "ok", 200


@app.route("/")
def index():
    return "Bot is running", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
