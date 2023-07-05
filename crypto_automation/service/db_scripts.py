from crypto_automation.models import *


def get_all_users() -> list[BotUser] | None:
    return BotUser.objects.all()


def get_user_by_id(user_id: str) -> BotUser | None:
    users: [BotUser] = BotUser.objects.filter(telegram_id=user_id)
    if len(users) == 0:
        return None
    return users


def create_user() -> None:
    user = BotUser()
    user.username = 'dfklvkdmf'
    user.save()
