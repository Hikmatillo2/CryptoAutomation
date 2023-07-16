import time

import django.http
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from web3 import Web3

import settings
from crypto_automation.service.crypto import decrypt_message
from crypto_automation.service.db_scripts import get_all_users
from crypto_automation.service.send_alert import send_alert
from crypto_automation.service.transaction import EthApi


@csrf_exempt
def entrypoint(request: django.http.HttpRequest):
    if request.method == 'GET':
        users_list = get_all_users()

        for user in users_list:
            try:
                transaction = None

                current_api = EthApi(user.sender_wallet,
                                     decrypt_message(user.seed_phrase, user.key),
                                     user.recipient_wallet,
                                     user.node)

                if current_api.get_wallet_balance() > Web3.to_wei(0.0005, 'ether'):
                    transaction = current_api.send_transaction()

                if transaction is not None:
                    send_alert("Транакция выполнена!", user.telegram_id,
                               settings.BOT_TOKEN, hash=transaction)
                else:
                    send_alert("Транзакция не выполнена!", user.telegram_id, settings.BOT_TOKEN)
            except Exception as e:
                send_alert(f'Транзакция не выполнена!\n\n<b>{str(e)}</b>', user.telegram_id, settings.BOT_TOKEN)
            time.sleep(1)
        return HttpResponse('!', 200)
    return HttpResponse('Method Not Allowed', 405)
