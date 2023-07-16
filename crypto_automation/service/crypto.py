from cryptography.fernet import Fernet


# Генерация случайного ключа шифрования
def generate_key():
    key = Fernet.generate_key()
    return key.decode("ascii")


# Шифрование строки
def encrypt_message(message, key):
    key = bytes(key, 'ascii')
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode('ascii')).decode('ascii')
    return str(encrypted_message)


# Расшифровка строки
def decrypt_message(encrypted_message, key):
    key = bytes(key, 'ascii')
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode("ascii")).decode()
    return decrypted_message
