import uuid
from utils.database.queries import *

def GenerateReceiptUID():
    try:
        uid = uuid.uuid4().hex

        if uid == None:
            raise Exception("Failed to generate receipt UID")

        if query_existing_receiptUID(uid) is True:
            GenerateReceiptUID()

        return uid, 200
    
    except Exception as error:
        return f"[GenerateReceiptUID] {error}", 500 
