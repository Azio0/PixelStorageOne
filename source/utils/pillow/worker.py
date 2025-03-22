import io
import base64
from PIL import Image

from utils.database.queries import *
from utils.transaction.worker import *

def DeconstructImage(image_path):
    try:
        image = Image.open(image_path).convert(ConfigParser('pillow', 'color'))
        img_byte_arr = io.BytesIO()

        image.save(img_byte_arr, format=ConfigParser('pillow', 'format'))
        img_byte_arr = img_byte_arr.getvalue()

        base64_str = base64.b64encode(img_byte_arr).decode('utf-8')

        receiptUID, receiptStatus = GenerateReceiptUID()

        if receiptStatus != 200:
            raise Exception(receiptUID)

        filename = Image.open(image_path).filename.split('/')[-1]

        response, status = insert_image_data(receiptUID, filename, base64_str)

        if status == 200:
            return receiptUID, 200
        
        else:
            raise Exception(response)

    except Exception as error:
        return f"[DeconstructImage] {error}", 500

def RetrieveImage(receiptUID):
    try:
        base64_str = retrieve_image_data(receiptUID)[0][3]

        image = Image.open(io.BytesIO(base64.b64decode(base64_str)))

        return image, 200
    except Exception as error:
        return f"[RetrieveImage] {error}", 500
