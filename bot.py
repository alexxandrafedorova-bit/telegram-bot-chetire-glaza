from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_http_server():
    server = HTTPServer(("0.0.0.0", 10000), PingHandler)
    server.serve_forever()

threading.Thread(target=run_http_server, daemon=True).start()
import telebot
from telebot import types

TOKEN = "8406532654:AAGnWgd8Ox8RpiDBZzk_TBXE-xgQi6nxUgs"
SITE_URL = "https://4glaza-72.ru"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)

    webapp_button = types.InlineKeyboardButton(
        text="🛒 Оформить заказ",
        web_app=types.WebAppInfo(url=SITE_URL)
    )

    manager_button = types.InlineKeyboardButton(
        text="💬 Написать менеджеру",
        url="https://t.me/Four_eyes72"
    )

    call_button = types.InlineKeyboardButton(
        text="📞 Позвонить",
        url="tel:+79220013072"
    )

    address_button = types.InlineKeyboardButton(
        text="📍 Адрес",
        callback_data="address"
    )

    time_button = types.InlineKeyboardButton(
        text="⏰ Время работы",
        callback_data="time"
    )

    markup.add(
        webapp_button,
        manager_button,
        call_button,
        address_button,
        time_button
    )

    bot.send_message(
        message.chat.id,
        "👋 Здравствуйте!\n\n"
        "Добро пожаловать в «Четыре глаза» 👓\n"
        "Вы можете оформить заказ прямо в Telegram или связаться с нами удобным способом:",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "address")
def send_address(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "📍 Наш адрес:\n"
        "г. Тюмень, ул. 50 лет Октября, 29"
    )


@bot.callback_query_handler(func=lambda call: call.data == "time")
def send_time(call):
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "⏰ Время работы:\n"
        "Ежедневно с 10:00 до 20:00"
    )

bot.polling()