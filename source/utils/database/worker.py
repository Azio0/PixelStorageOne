import mysql.connector
from mysql.connector import Error

from utils.config.worker import ConfigParser

def create_connection():
    try:
        connection = mysql.connector.connect(
            host=ConfigParser('database', 'host'),
            user=ConfigParser('database', 'user'),
            password=ConfigParser('database', 'password'),
            database=ConfigParser('database', 'database'),
            port=ConfigParser('database', 'port')
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
