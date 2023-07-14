from django.db import models


# null=True адрес кошелька, с которого будут совершаться
# транзакции seed-phrase для доступа к кошельку адрес кошелька, на который будут поступать eth
class BotUser(models.Model):
    username = models.CharField(max_length=20, null=True,
                                help_text='Введите имя пользователя. Максимсальная длина - 20')

    sender_wallet = models.CharField(max_length=50,
                                     null=True,
                                     help_text='адрес кошелька(0x...), с которого будут совершаться транзакции')

    phrase = models.TextField(null=True,
                              help_text='seed-phrase для доступа к кошельку')

    recipient_wallet = models.CharField(max_length=50,
                                        null=True,
                                        help_text='адрес кошелька(0x...), на который будут поступать eth')

    node = models.TextField(null=True,
                            help_text='введите адресс ноды (https://chainlist.org/?search=eth)')

    telegram_id = models.CharField(max_length=30,
                                   null=True,)

    class Meta:
        verbose_name_plural = 'Users data'
