import telebot
from telebot import types

TOKEN = "8406532654:AAGnWgd8Ox8RpiDBZzk_TBXE-xgQi6nxUgs"
SITE_URL = "https://4glaza-72.ru"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()

    webapp_button = types.InlineKeyboardButton(
        text="🛒 Оформить заказ",
        web_app=types.WebAppInfo(url=SITE_URL)
    )

    manager_button = types.InlineKeyboardButton(
        text="💬 Написать менеджеру",
        url="https://t.me/Four_eyes72?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5!%20%D0%AF%20%D0%BF%D0%B8%D1%88%D1%83%20%D0%B8%D0%B7%20Telegram-%D0%B1%D0%BE%D1%82%D0%B0%20%C2%AB%D0%A7%D0%B5%D1%82%D1%8B%D1%80%D0%B5%20%D0%B3%D0%BB%D0%B0%D0%B7%D0%B0%C2%BB."
    )

    markup.add(webapp_button)
    markup.add(manager_button)

    bot.send_message(
        message.chat.id,
        "Здравствуйте! 👋\n\n"
        "Добро пожаловать в «Четыре глаза» 🔭\n"
        "Вы можете оформить заказ прямо в Telegram:",
        reply_markup=markup
    )


bot.polling()