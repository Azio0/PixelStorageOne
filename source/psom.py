from utils.config.worker import *
from utils.database.worker import *
from utils.database.queries import *
from utils.pillow.worker import *
from utils.transaction.worker import *
from utils.ziparchive.worker import *

class PixelStorageOne:
    class deconstruct:
        def Image(image_path):
            try:
                response, status = DeconstructImage(image_path)

                if status != 200:
                    raise Exception(f'Error {response}')
                
                return response, status
            
            except Exception as error:
                return error, 500

        def ZipFile(zip_path):
            try:
                response, status = DeconstructZipFile(zip_path)

                if status != 200:
                    raise Exception(f'Error {response}')

                return response, status
            
            except Exception as error:
                return error, 500
        
    class retrieve:
        def Image(receiptUID):
            try:
                response, status = RetrieveImage(receiptUID)

                if status != 200:
                    raise Exception(f'Error {response}')
                
                return response, status
        
            except Exception as error:
                return error, 500
            
        def ZipFile(receiptUID):
            try:
                response, status = RetrieveZipFile(receiptUID)

                if status != 200:
                    raise Exception(f'Error {response}')
                
                return response, status
            
            except Exception as error:
                return error, 500
