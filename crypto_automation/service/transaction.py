from web3 import Web3
from db_scripts import get_data_of_single_user

# https://rpc2.sepolia.org - node of eth testnet
# https://eth.llamarpc.com - node of ethereum mainnet

eth_node = 'https://rpc2.sepolia.org'
node = Web3(Web3.HTTPProvider(eth_node))

user = get_data_of_single_user(0)

sender_address = user['sender_wallet']
recipient_address = user['recipient_wallet']
phrase = user['sender_seed_phrase']

sender_key = phrase
checksum_sender = Web3.to_checksum_address(sender_address)
checksum_recipient = Web3.to_checksum_address(recipient_address)
gas = node.eth.gas_price

start_balance = node.eth.get_balance(checksum_sender)

while True:
    current_balance = node.eth.get_balance(checksum_sender)

    if(current_balance > start_balance):
        amount = current_balance - start_balance
        gas_price = node.eth.gas_price

        transaction = {
            'chainId': 11155111,
            'from': checksum_sender,
            'to': checksum_recipient,
            'value': amount,
            'gas': 210000,
            'gasPrice': gas_price,
            'nonce': node.eth.get_transaction_count(checksum_sender)
        }

        signed_transaction = node.eth.account.sign_transaction(transaction, sender_key)

        transaction_hash = node.eth.send_raw_transaction(signed_transaction.rawTransaction)

        start_balance = node.eth.get_balance(checksum_sender)