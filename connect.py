import mysql.connector
from mysql.connector import Error

def connect_db():
    """Connects to the MySQL database and returns the connection object."""
    try:
        connection = mysql.connector.connect(
            host='buyam.co',
            port=3306,
            user='read',
            password='Onesaint02@',
            database='buyam'
        )
        if connection.is_connected():
            print("Successfully connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None
