from web3 import Web3
from web3.middleware import geth_poa_middleware
from settings import DEBUG


# https://rpc2.sepolia.org - node of eth testnet
# https://eth.llamarpc.com - node of ethereum mainnet


class EthApi:
    def __init__(self, sender_address: str, seed_phrase: str, recipient_address: str, node: str):
        self.node = Web3(Web3.HTTPProvider(node))
        self.seed_phrase = seed_phrase  # Account.from_mnemonic(seed_phrase).privateKey.hex()
        self.sender_address = Web3.to_checksum_address(sender_address)
        self.recipient_address = Web3.to_checksum_address(recipient_address)

    def get_key_from_mnemonic(self):
        if len(self.seed_phrase.split()) > 2:
            self.node.middleware_onion.inject(geth_poa_middleware, layer=0)
            self.node.eth.account.enable_unaudited_hdwallet_features()

            account = self.node.eth.account.from_mnemonic(self.seed_phrase)
            private_key = account.key.hex()  # hex адрес
            return private_key

        return self.seed_phrase

    def get_gas(self):
        return self.node.eth.gas_price + 1000000

    def get_estimated_gas(self):
        return self.node.eth.estimate_gas({'from': self.sender_address,
                                           'to': self.recipient_address
                                           })

    def get_wallet_balance(self):
        return self.node.eth.get_balance(self.sender_address)  # wei gwei eth

    def compile_transaction(self, amount: int) -> dict:
        return {
            'chainId': self.node.eth.chain_id,
            'from': self.sender_address,
            'to': self.recipient_address,
            'value': amount,
            'gas': self.get_estimated_gas(),
            'gasPrice': self.get_gas(),
            'nonce': self.node.eth.get_transaction_count(self.sender_address)
        }

    def sign_transaction(self, amount: int):
        return self.node.eth.account.sign_transaction(self.compile_transaction(amount), self.get_key_from_mnemonic())

    def send_transaction(self) -> str:
        amount = self.get_wallet_balance() - self.get_gas() * self.get_estimated_gas() - 1000

        return str(self.node.eth.send_raw_transaction(self.sign_transaction(amount).rawTransaction).hex())
