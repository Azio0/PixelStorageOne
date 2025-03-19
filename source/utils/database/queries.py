from utils.database.worker import *

def create_table():
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
        return f"[create_table] {error}", 500

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

def return_tables():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SHOW TABLES
            """
        )
        return cursor.fetchall()

    except Exception as error:
        return f"[return_tables] {error}", 500

def return_all_data():
    try:
        connection = create_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT * FROM image_data
            """
        )
        return cursor.fetchall()
    
    except Exception as error:
        return f"[return_all_data] {error}", 500
    
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

def delete_all_data():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            DELETE FROM image_data
            """
        )
        connection.commit()

        return "Deleted all data", 200
    
    except Exception as error:
        return f"[delete_all_data] {error}", 500
    
def delete_tables():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            DROP TABLE image_data
            """
        )
        connection.commit()

        return "Deleted all tables", 200
    
    except Exception as error:
        return f"[delete_all_tables] {error}", 500

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
