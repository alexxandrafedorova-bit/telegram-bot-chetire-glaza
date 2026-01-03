import os
import telebot
from telebot import types
from flask import Flask, request

# ================== НАСТРОЙКИ ==================

TOKEN = os.getenv("BOT_TOKEN")  # токен берём из Render Environment
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # https://telegram-bot-chetire-glaza.onrender.com

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# ================== МЕНЮ ==================

def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    web_app = types.WebAppInfo(url="https://4glaza-72.ru")
    btn_order = types.KeyboardButton("🛒 Оформить заказ", web_app=web_app)

    btn_manager = types.KeyboardButton("💬 Написать менеджеру")
    btn_call = types.KeyboardButton("📞 Позвонить")
    btn_address = types.KeyboardButton("📍 Адрес")
    btn_time = types.KeyboardButton("⏰ Время работы")

    markup.add(btn_order)
    markup.add(btn_manager, btn_call)
    markup.add(btn_address, btn_time)

    return markup

# ================== START ==================

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в магазин «Четыре глаза» (Тюмень)\n\n"
        "🔭 Телескопы\n"
        "🔬 Микроскопы\n"
        "🔭 Бинокли\n\n"
        "Нажмите «🛒 Оформить заказ», чтобы открыть каталог.",
        reply_markup=main_menu()
    )

# ================== КНОПКИ ==================

@bot.message_handler(func=lambda message: message.text == "💬 Написать менеджеру")
def manager(message):
    bot.send_message(
        message.chat.id,
        "💬 Написать менеджеру:\n"
        "👉 https://t.me/Four_eyes72"
    )

@bot.message_handler(func=lambda message: message.text == "📞 Позвонить")
def call(message):
    bot.send_message(
        message.chat.id,
        "📞 Телефон магазина:\n"
        "+7 922 001-30-72\n\n"
        "Нажмите на номер, чтобы позвонить 📱"
    )

@bot.message_handler(func=lambda message: message.text == "📍 Адрес")
def address(message):
    bot.send_message(
        message.chat.id,
        "📍 Наш адрес:\n"
        "г. Тюмень, ул. 50 лет Октября, 29"
    )

@bot.message_handler(func=lambda message: message.text == "⏰ Время работы")
def time(message):
    bot.send_message(
        message.chat.id,
        "⏰ Время работы:\n"
        "Ежедневно\n"
        "С 10:00 до 20:00"
    )

# ================== WEBHOOK ==================

@app.route("/", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route("/", methods=["GET"])
def index():
    return "Bot is running", 200

# ================== ЗАПУСК ==================

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
