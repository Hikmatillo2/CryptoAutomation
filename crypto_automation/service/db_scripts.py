import os
import django
django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()
from crypto_automation.models import *

# def get_all_users() -> list[BotUser] | None:
#     return BotUser.objects.all()
#
#
# def get_user_by_id(user_id: str) -> BotUser | None:
#     users: [BotUser] = BotUser.objects.filter(telegram_id=user_id)
#     if len(users) == 1:
#         return None
#     return users
#
#
# def create_user() -> None:
#     user = BotUser()
#     user.username = 'dfklvkdmf'
#     user.save()

def get_data_of_single_user(id: int) -> dict:
    user = BotUser.objects.all()[id]
    data = {'sender_wallet': user.sender_wallet,
            'sender_seed_phrase': user.phrase,
            'recipient_wallet': user.recipient_wallet
            }
    return data

print(get_data_of_single_user(0))