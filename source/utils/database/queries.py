from utils.database.worker import *

def create_table():
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS image_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                recieptUID VARCHAR(9000) NOT NULL,
                filename VARCHAR(256) NOT NULL,
                imagedata LONGTEXT NOT NULL
            )
            """
        )
        connection.commit()

        return "Table created", 200
    
    except Exception as error:
        return f"[create_table] {error}", 500

def insert_image_data(recieptUID, filename, y):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO image_data (recieptUID, filename, imagedata)
            VALUES (%s, %s, %s)
            """,
            (recieptUID, filename, y)
        )
        connection.commit()

        return f"Inserted {recieptUID}", 200
    
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
    
def retrieve_image_data(recieptUID):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT * FROM image_data WHERE recieptUID = %s
            """,
            (recieptUID,)
        )
        return cursor.fetchall()
    
    except Exception as error:
        return f"[retrieve_image_data] {error}", 500

def delete_image_data(recieptUID):
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            DELETE FROM image_data WHERE recieptUID = %s
            """,
            (recieptUID,)
        )
        connection.commit()

        return f"Deleted {recieptUID}", 200
    
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
