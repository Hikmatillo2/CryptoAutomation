from django import forms
from .models import *


class ServerForm(forms.ModelForm):
    class Meta:
        model = BotUser
        fields = ('username',
                  'sender_wallet',
                  'seed_phrase',
                  'recipient_wallet',
                  'node',
                  'telegram_id')
