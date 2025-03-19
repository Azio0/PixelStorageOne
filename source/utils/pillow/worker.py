import io
import base64
import random
from PIL import Image

from utils.database.queries import *

def DeconstructImage(image_path):
    try:
        image = Image.open(image_path).convert("RGB")
        img_byte_arr = io.BytesIO()

        image.save(img_byte_arr, format="PNG")
        img_byte_arr = img_byte_arr.getvalue()

        base64_str = base64.b64encode(img_byte_arr).decode('utf-8')

        recieptUID = random.randint(0, 9000)

        filename = Image.open(image_path).filename.split('/')[-1]

        response, status = insert_image_data(recieptUID, filename, base64_str)

        if status == 200:
            return recieptUID, 200
        
        else:
            raise Exception(response)

    except Exception as error:
        return f"[DeconstructImage] {error}", 500

def RetrieveImage(recieptUID):
    try:
        base64_str = retrieve_image_data(recieptUID)[0][3]

        print(base64_str)

        image = Image.open(io.BytesIO(base64.b64decode(base64_str)))

        return image, 200
    except Exception as error:
        return f"[RetrieveImage] {error}", 500
