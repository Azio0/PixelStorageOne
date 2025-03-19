import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='www.example.com',
            user='example',
            password='example',
            database='example_database',
            port='3306',
        )
        if connection.is_connected():
            return connection

    except Error as error:
        return f"[create_connection] Error: {error}", 500

def close_connection(connection):
    if connection.is_connected():
        connection.close()

def retrieve_connection():
    return create_connection()
