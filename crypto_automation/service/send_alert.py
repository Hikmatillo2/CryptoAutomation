from telebot import TeleBot
from telebot.types import Message


def send_alert(message: str, telegram_id: str, token: str):
    try:
        bot = TeleBot(token)

        bot.send_message(telegram_id, message)
    except:
        pass
