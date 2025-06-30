# connect_mysql_securely.py
import mysql.connector
from password_security import get_decrypted_password

#connect to MYSQL using the decrypted (but masked) password
def connect_to_mysql():
    db = None
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=get_decrypted_password(),
            database="tea_business"
)
        print("Connected to MySQL database!")
#prints masked ******
        print(get_decrypted_password())
        cursor = db.cursor()
        cursor.execute("select database();")
        print("current database:",cursor.fetchone()[0])
    except mysql.connector.Error as err:
        print("mysql error:",err)
    finally:
        if db and db.is_connected():
#closes only if opened
            db.close()
            print("connection closed")

if __name__ == '__main__':
    connect_to_mysql()