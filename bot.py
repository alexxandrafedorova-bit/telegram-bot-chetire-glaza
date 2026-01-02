import telebot
from telebot import types

TOKEN = "8406532654:AAGnWgd8Ox8RpiDBZzk_TBXE-xgQi6nxUgs"

bot = telebot.TeleBot(TOKEN)


# ---------- МЕНЮ ----------
def main_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # КНОПКА С МИНИ-ПРИЛОЖЕНИЕМ
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


# ---------- /start ----------
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Добро пожаловать в магазин «Четыре глаза» (Тюмень)\n\n"
        "🔭 Телескопы\n"
        "🔬 Микроскопы\n"
        "🔭 Бинокли\n\n"
        "Нажмите «Оформить заказ», чтобы открыть каталог.",
        reply_markup=main_menu()
    )


# ---------- КНОПКИ ----------
@bot.message_handler(func=lambda message: message.text == "💬 Написать менеджеру")
def manager(message):
    bot.send_message(
        message.chat.id,
        "💬 Менеджер магазина:\n"
        "👉 @Four_eyes72\n\n"
        "Сообщение можно начать так:\n"
        "«Здравствуйте! Хочу оформить заказ»"
    )


@bot.message_handler(func=lambda message: message.text == "📞 Позвонить")
def call(message):
    bot.send_message(
        message.chat.id,
        "📞 Телефон магазина:\n"
        "+7 (922) 001-30-72"
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
        "С 10:00 до 20:00\n"
        "Ежедневно"
    )


# ---------- ЗАПУСК ----------
bot.polling(none_stop=True)