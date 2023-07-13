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


def get_all_users():
    users = BotUser.objects.all()

    if len(users) == 0:
        return None

    return users


user = get_all_users()[0]

print(user.sender_wallet)
