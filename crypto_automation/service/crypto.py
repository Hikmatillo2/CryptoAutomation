from cryptography.fernet import Fernet


# Генерация случайного ключа шифрования
def generate_key():
    key = Fernet.generate_key()
    return key


# Шифрование строки
def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message


# Расшифровка строки
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Пример использования
