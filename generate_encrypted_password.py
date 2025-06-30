# generate_encrypted_password.py
from  password_security import encrypt_password
from cryptography.fernet import Fernet
import getpass

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    print("Key saved to secret.key")

if __name__ == "__main__":
    # 🔓 Run only ONCE to generate the key file
    #generate_key()
    #securely take password input at runtime(nothing is shown while typing)
    password = getpass.getpass("enter your mysql password to encrypt:")

    # 🔐 Replace with your real MySQL password
    encrypted = encrypt_password(password)
    print("Encrypted password (copy this to password.enc):")
    print(encrypted)
