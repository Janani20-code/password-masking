# password_security.py
from cryptography.fernet import Fernet

class FakeStr(str):
    def __str__(self):
        return "********"
    def __repr__(self):
        return "*******"
#load the secret key
def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())
#decrypt the password and return a protected string

def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)
def get_decrypted_password():
    key = load_key()
    f = Fernet(key)
    encrypted_password = open("password.enc", "rb").read()
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)