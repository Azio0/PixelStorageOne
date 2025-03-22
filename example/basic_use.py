import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'source')))

from psom import PixelStorageOne

# Create an instance of the PixelStorageOne class
PSO = PixelStorageOne()

# Image deconstruction and retrieval
def image(x):
    # Deconstruct an image
    receiptUID, status = PSO.deconstruct.Image(x)
    print(receiptUID, status)

    if status != 200:
        return f"Error: {receiptUID}"

    # Retrieve an image
    image_data, status = PSO.retrieve.Image(receiptUID)
    print(image_data, status)

    if status != 200:
        return f"Error: {image_data}"

    return "Image deconstruction and retrieval successful"

# Zip file deconstruction and retrieval
def zip_file(y):
    # Deconstruct a zip file
    receiptUID, status = PSO.deconstruct.ZipFile(y)
    print(receiptUID, status)

    if status != 200:
        return f"Error: {receiptUID}"

    # Retrieve a zip file
    zip_data, status = PSO.retrieve.ZipFile(receiptUID)
    print(zip_data, status)

    if status != 200:
        return f"Error: {zip_data}"
    
    return "Zip file deconstruction and retrieval successful"

image_path = input('Image Path: > ')
image_example = image(image_path)

print(image_example)

zip_path = input('Zip Path: > ')
zip_example = zip_file(zip_path)

print(zip_example)
