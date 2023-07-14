from ..models import BotUser


def get_all_users():
    users = BotUser.objects.all()

    if len(users) == 0:
        return None

    return users
