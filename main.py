import os
from flask import Flask, request
import telebot
from telebot import types

TOKEN = os.getenv("BOT_TOKEN")  # токен хранится в Render
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


# ---------- МЕНЮ ----------
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    web_app = types.WebAppInfo(url="https://4glaza-72.ru")
    btn_order = types.KeyboardButton("🛒 Оформить заказ", web_app=web_app)

    btn_call = types.KeyboardButton("📞 Позвонить")
    btn_address = types.KeyboardButton("📍 Адрес")
    btn_time = types.KeyboardButton("⏰ Время работы")

    markup.add(btn_order)
    markup.add(btn_call)
    markup.add(btn_address, btn_time)

    return markup


# ---------- /start ----------
@bot.message_handler(commands=["start"])
def start(message):
    inline = types.InlineKeyboardMarkup()
    inline.add(
        types.InlineKeyboardButton(
            "💬 Написать менеджеру",
            url="https://t.me/Four_eyes72"
        )
    )

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в магазин «Четыре глаза» (Тюмень)\n\n"
        "🔭 Телескопы\n"
        "🔬 Микроскопы\n"
        "🔭 Бинокли\n\n"
        "Нажмите «Оформить заказ», чтобы открыть каталог.",
        reply_markup=main_menu()
    )

    bot.send_message(
        message.chat.id,
        "Если нужна консультация — напишите менеджеру 👇",
        reply_markup=inline
    )


# ---------- КНОПКИ ----------
@bot.message_handler(func=lambda message: message.text == "📞 Позвонить")
def call(message):
    bot.send_message(
        message.chat.id,
        "📞 Телефон магазина:\n+7 (922) 001-30-72"
    )


@bot.message_handler(func=lambda message: message.text == "📍 Адрес")
def address(message):
    bot.send_message(
        message.chat.id,
        "📍 Наш адрес:\nг. Тюмень, ул. 50 лет Октября, 29"
    )


@bot.message_handler(func=lambda message: message.text == "⏰ Время работы")
def time(message):
    bot.send_message(
        message.chat.id,
        "⏰ Время работы:\nС 10:00 до 20:00\nЕжедневно"
    )


# ---------- WEBHOOK ----------
@app.route("/", methods=["GET"])
def index():
    return "Bot is running"


@app.route("/webhook", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok"
