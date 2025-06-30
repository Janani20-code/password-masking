# 🔐 Password Masking (Python + MySQL)

A secure way to store and use MySQL passwords using *Fernet encryption* in Python.  
This prevents exposing credentials directly in your code and promotes safe development practices.

## 💻 Tech Used

- Python 3
- MySQL
- cryptography (Fernet)
- PyCharm

## 📁 Project Files

| File Name                    | Purpose                                            |
|------------------------------|----------------------------------------------------|
| encrypt_once.py              | Generates secret.key and encrypted password.       |
| password_security.py         | Encrypts and decrypts the password securely.       |
| connect_mysql-securely.py    | Connects to MySQL using the decrypted password.    |
| secret.key & password.enc    | Sensitive encrypted credentials (keep safe!)       |

### Install Required Packages

```bash
pip install cryptography mysql-connector-python
```

## 🙌 Credits

*Special thanks to [Gowtham SB](https://www.linkedin.com/in/sbgowtham/)*
for sharing such valuable knowledge through your YouTube tutorials.  

This project is inspired by your explanation of password masking in Python.  
It helped me build my *first real-world project* with a focus on *secure coding practices*.  
Grateful for the clarity and guidance you provide in your content!
