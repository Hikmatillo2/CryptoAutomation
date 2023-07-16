from django.contrib import admin
from .models import BotUser
from .forms import ServerForm



@admin.register(BotUser)  # дикоратор(@) - f, которая принимает f и исполняет ее внутри себя, дополнительно насыщая кодом
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['username'
                    ]

    form = ServerForm
