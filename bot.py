import os
import telebot
from telebot import types
from flask import Flask, request

# ====== НАСТРОЙКИ ======
TOKEN = os.getenv("BOT_TOKEN")  # токен из Render Environment
MANAGER_USERNAME = "Four_eyes72"

WEBHOOK_URL = "https://telegram-bot-chetire-glaza.onrender.com"

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


# ====== МЕНЮ ======
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    web_app = types.WebAppInfo(url="https://4glaza-72.ru")
    btn_order = types.KeyboardButton("🛒 Оформить заказ", web_app=web_app)

    btn_manager = types.InlineKeyboardButton(
        text="💬 Написать менеджеру",
        url=f"https://t.me/{MANAGER_USERNAME}"
    )

    btn_call = types.KeyboardButton("📞 Позвонить")
    btn_address = types.KeyboardButton("📍 Адрес")
    btn_time = types.KeyboardButton("⏰ Время работы")

    markup.add(btn_order)
    markup.add(btn_call)
    markup.add(btn_address, btn_time)

    inline = types.InlineKeyboardMarkup()
    inline.add(btn_manager)

    return markup, inline


# ====== /start ======
@bot.message_handler(commands=["start"])
def start(message):
    menu, inline = main_menu()

    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в магазин «Четыре глаза» (Тюмень)\n\n"
        "🔭 Телескопы\n"
        "🔬 Микроскопы\n"
        "🔭 Бинокли\n\n"
        "Нажмите «Оформить заказ», чтобы открыть каталог.",
        reply_markup=menu
    )

    bot.send_message(
        message.chat.id,
        "Если нужен менеджер — нажмите кнопку ниже 👇",
        reply_markup=inline
    )


# ====== КНОПКИ ======
@bot.message_handler(func=lambda m: m.text == "📞 Позвонить")
def call(message):
    bot.send_message(message.chat.id, "📞 +7 (922) 001-30-72")


@bot.message_handler(func=lambda m: m.text == "📍 Адрес")
def address(message):
    bot.send_message(
        message.chat.id,
        "📍 г. Тюмень, ул. 50 лет Октября, 29"
    )


@bot.message_handler(func=lambda m: m.text == "⏰ Время работы")
def time(message):
    bot.send_message(
        message.chat.id,
        "⏰ Ежедневно с 10:00 до 20:00"
    )


# ====== WEBHOOK ======
@server.route("/", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200


@server.route("/")
def index():
    return "Bot is running"


# ====== ЗАПУСК ======
if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    server.run(host="0.0.0.0", port=10000)
