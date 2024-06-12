import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load environment variables from .env file
load_dotenv()

class DatabaseConnector:
    def __init__(self):
        self.connection = None

    def connect_db(self):
        """Connects to the MySQL database and returns the connection object."""
        try:
            self.connection = mysql.connector.connect(
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                port=int(os.getenv('DB_PORT')),
                database=os.getenv('DB_NAME')
            )
            if self.connection.is_connected():
                print("Successfully connected to the database")
        except Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        """Closes the database connection."""
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("Connection closed")

    def get_connection(self):
        """Returns the database connection object."""
        return self.connection

