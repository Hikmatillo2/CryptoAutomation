# Generated by Django 4.2.1 on 2023-07-14 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_automation', '0014_alter_botuser_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='node',
            field=models.TextField(help_text='введите адресс ноды', null=True),
        ),
    ]