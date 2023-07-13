import os
import django
django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()
from web3 import Web3
from eth_account import Account
from db_scripts import get_all_users

# https://rpc2.sepolia.org - node of eth testnet
# https://eth.llamarpc.com - node of ethereum mainnet


class EthApi:
    def __init__(self, sender_address: str, seed_phrase: str, recipient_address: str, node: str):
        self.node = Web3(Web3.HTTPProvider(node))
        self.private_key = seed_phrase  # Account.from_mnemonic(seed_phrase).privateKey.hex()
        self.sender_address = Web3.to_checksum_address(sender_address)
        self.recipient_address = Web3.to_checksum_address(recipient_address)

    def get_gas(self):
        return self.node.eth.gas_price + 1000

    def get_estimated_gas(self):
        return self.node.eth.estimate_gas({'from': self.sender_address,
                                           'to': self.recipient_address
                                           })

    def get_wallet_balance(self):
        return self.node.eth.get_balance(self.sender_address) #wei gwei eth

    def compile_transaction(self, amount: int) -> dict:
        return {
            'chainId': self.node.eth.chain_id,
            'from': self.sender_address,
            'to': self.recipient_address,
            'value': amount,
            'gas': 21000,
            'gasPrice': self.get_gas(),
            'nonce': self.node.eth.get_transaction_count(self.sender_address)
        }

    def sign_transaction(self, amount: int):
        return self.node.eth.account.sign_transaction(self.compile_transaction(amount), self.private_key)

    def send_transaction(self) -> str:
        amount = self.get_wallet_balance() - self.get_gas() * self.get_estimated_gas()

        return str(self.node.eth.send_raw_transaction(self.sign_transaction(amount).rawTransaction).hex())


def entrypoint(node: str):
    users_list = get_all_users()

    for user in users_list:
        try:
            transaction = None

            current_api = EthApi(user.sender_wallet,
                                 user.phrase,
                                 user.recipient_wallet,
                                 node)

            if current_api.get_wallet_balance() > Web3.to_wei(0.001, 'ether'):
                transaction = current_api.send_transaction()

            if transaction is not None:
                print(f'Successes! transaction hash is {transaction}')

        except Exception as e:
            print('хуево')


entrypoint('https://rpc2.sepolia.org')
