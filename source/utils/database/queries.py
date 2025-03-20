from utils.database.worker import *

def create_image_table():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS image_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                receiptUID VARCHAR(9000) NOT NULL,
                filename VARCHAR(256) NOT NULL,
                imagedata LONGTEXT NOT NULL
            )
            """
        )
        connection.commit()

        return "Table created", 200
    
    except Exception as error:
        return f"[create_image_table] {error}", 500

def insert_image_data(receiptUID, filename, y):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO image_data (receiptUID, filename, imagedata)
            VALUES (%s, %s, %s)
            """,
            (receiptUID, filename, y)
        )
        connection.commit()

        return f"Inserted {receiptUID}", 200
    
    except Exception as error:
        return f"[insert_image_data] {error}", 500
    
def retrieve_image_data(receiptUID):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM image_data WHERE receiptUID = %s
            """,
            (receiptUID,)
        )
        return cursor.fetchall()
    
    except Exception as error:
        return f"[retrieve_image_data] {error}", 500

def delete_image_data(receiptUID):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            DELETE FROM image_data WHERE receiptUID = %s
            """,
            (receiptUID,)
        )
        connection.commit()

        return f"Deleted {receiptUID}", 200
    
    except Exception as error:
        return f"[delete_image_data] {error}", 500

def query_existing_receiptUID(receiptUID):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT receiptUID FROM image_data WHERE receiptUID = %s
            """,
            (receiptUID,)
        )

        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True
    
    except Exception as error:
        return f"[query_existing_receiptUID] {error}", 500

def create_zip_table():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS zip_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                receiptUID VARCHAR(9000) NOT NULL,
                filename VARCHAR(256) NOT NULL,
                zipdata LONGTEXT NOT NULL
            )
            """
        )
        connection.commit()

        return "Table created", 200
    
    except Exception as error:
        return f"[create_zip_table] {error}", 500

def insert_zip_data(receiptUID, filename, y):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO zip_data (receiptUID, filename, zipdata)
            VALUES (%s, %s, %s)
            """,
            (receiptUID, filename, y)
        )
        connection.commit()

        return f"Inserted {receiptUID}", 200
    
    except Exception as error:
        return f"[insert_zip_data] {error}", 500
    
def retrieve_zip_data(receiptUID):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM zip_data WHERE receiptUID = %s
            """,
            (receiptUID,)
        )
        return cursor.fetchall(), 200
    
    except Exception as error:
        return f"[retrieve_zip_data] {error}", 500
