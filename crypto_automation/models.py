from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from crypto_automation.service.crypto import generate_key, encrypt_message


# null=True адрес кошелька, с которого будут совершаться
# транзакции seed-phrase для доступа к кошельку адрес кошелька, на который будут поступать eth
class BotUser(models.Model):
    username = models.CharField(max_length=20, null=True,
                                help_text='Введите имя пользователя. Максимсальная длина - 20')

    sender_wallet = models.CharField(max_length=50,
                                     null=True,
                                     help_text='адрес кошелька(0x...), с которого будут совершаться транзакции')

    seed_phrase = models.TextField(null=True,
                                   help_text='seed-phrase для доступа к кошельку')

    recipient_wallet = models.CharField(max_length=50,
                                        null=True,
                                        help_text='адрес кошелька(0x...), на который будут поступать eth')

    node = models.TextField(null=True,
                            help_text='введите адресс ноды (https://chainlist.org/?search=eth)')

    telegram_id = models.CharField(max_length=30,
                                   null=True,
                                   verbose_name='ID аккаунта в телеграме')

    key = models.CharField(max_length=100,
                           null=True)

    class Meta:
        verbose_name_plural = 'Users data'


@receiver(post_save, sender=BotUser)  # выполняется, когда нажали кнопку сохранить
def generate_hash(sender, instance, created, *args, **kwargs):
    if len(instance.seed_phrase.split()) > 2:
        instance.key = generate_key()
        instance.seed_phrase = encrypt_message(instance.seed_phrase, instance.key)
        instance.save()
