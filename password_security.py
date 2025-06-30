# password_security.py
from cryptography.fernet import Fernet

#hides the password when printed or represented
class FakeStr(str):
    def __str__(self):
        return "********"
    def __repr__(self):
        return "*******"

#load the encryption key from 'secret.key' file
def load_key():
    return open("secret.key", "rb").read()

#encrypt the given plain text password
def encrypt_password(password):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(password.encode())

#decrypt the encrypted password and return it as masked string
def decrypt_password(encrypted_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)

#get the decrypted password from 'password.enc'
def get_decrypted_password():
    key = load_key()
    f = Fernet(key)
    encrypted_password = open("password.enc", "rb").read()
    decrypted = f.decrypt(encrypted_password).decode()
    return FakeStr(decrypted)