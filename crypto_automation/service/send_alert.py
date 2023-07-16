from telebot import TeleBot
from telebot.types import Message
from settings import TRANSACTION_INFO_URL


def send_alert(message: str, telegram_id: str, token: str, hash: str = None):
    bot = TeleBot(token)

    try:

        if hash is not None:
            message += f"\n\n <a href='{TRANSACTION_INFO_URL}{hash}'>Информация о транзакции</a>"

        bot.send_message(telegram_id, message, parse_mode='html')
    except Exception as e:
        bot.send_message(telegram_id, str(e))
