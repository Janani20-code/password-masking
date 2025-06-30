# mysql_connect_safe.py
import mysql.connector
from password_utils import get_decrypted_password
def connect_to_mysql() -> None:
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password=get_decrypted_password(),
            database="tea_business"
)

        print("Connected to MySQL database!")
        print(get_decrypted_password())
        cursor = db.cursor()
        cursor.execute("select database();")
        print("current database:",cursor.fetchone()[0])
    except mysql.connector.Error as err:
        print("mysql error:",err)
    finally:
        if db.is_connected():
            db.close()
            print("connection closed")

if __name__ == '__main__':
    connect_to_mysql()