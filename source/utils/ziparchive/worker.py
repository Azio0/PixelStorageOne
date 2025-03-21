import os
import base64

from utils.transaction.worker import *

def DeconstructZipFile(zip_path):
    try:
        if zip_path.split('.')[-1] != 'zip':
            raise Exception("File must be a zip archive")

        if not os.path.exists(zip_path):
            raise Exception(f"No such archive named {zip_path}")

        with open(zip_path, 'rb') as file:
            binary_content = file.read()

        receiptUID, receiptStatus = GenerateReceiptUID()

        if receiptStatus != 200:
            raise Exception(receiptUID)
        
        filename = zip_path.split('/')[-1]

        encoded_binary = base64.b64encode(binary_content)

        response, status = insert_zip_data(receiptUID, filename, encoded_binary)

        if status != 200:
            raise Exception(response)

        return receiptUID, 200
    
    except Exception as error:
        return f"[DeconstructZipFile] {error}", 500

def RetrieveZipFile(receiptUID):
    try:
        response, status = retrieve_zip_data(receiptUID)

        if status != 200:
            raise Exception(response)
        
        base64_encoded_zipdata = response[0][3]

        return base64_encoded_zipdata, 200
    except Exception as error:
        return f"[RetrieveZipFile] {error}", 500
