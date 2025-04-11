# PixelStorageOne

**PixelStorageOne** is an open-source utility for deconstructing and retrieving images and zip files. It provides a simple interface to store and retrieve binary data from a MySQL database, allowing the content to be easily accessed from another location, service or recalled on demand.

This can be used to handle storage for website images, file upload storage and more.

## Features

- The ability to store file data via a database
- Support for both image files and zip archives
- Easy to configure SQL credentials in the config file
- Flexible module to customise to fit your requirements
- Alternative low-cost storage of data compared to hosting services

## Requirements
- Python 3
- MySQL Database

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Azio0/PixelStorageOne.git
   cd PixelStorageOne
   ```
2. Install Python and PIP:
   ```bash
   sudo apt-get install python3
   sudo apt-get install python3-pip
   ```
4. Install the required Python Packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Modify the MySQL Database details:
   ```
   cd source/utils/config
   edit the databse section in config.yml
   ```

6. Call the setup database function on initial setup:
   ```
   make a .py file and import PixelStorageOne
   inside the file call PSO.setup.database()
   ```

8. Move the module into your source code, and reference PixelStorageOne to call the class methods. An example is below showcasing how this can be done.

## How It Works

PixelStorageOne uses the following components:
- **Configuration**: Reads configuration settings from a YAML file.
- **Database**: Manages connections and queries to a MySQL database.
- **Transaction**: Generates unique receipt UIDs for transactions.
- **Pillow**: Handles image processing and encoding.
- **ZipArchive**: Handles zip file processing and encoding.

## Class: `PixelStorageOne`

The `PixelStorageOne` class provides methods to deconstruct and retrieve images and zip files. It has two main nested classes: `deconstruct` and `retrieve`.

### Methods

#### `deconstruct.Image(image_path)`

Deconstructs an image file, encodes it in base64, and stores it in the database.

- **Parameters**: `image_path` (str) - The path to the image file.
- **Returns**: A tuple containing the receipt UID and status code.

#### `deconstruct.ZipFile(zip_path)`

Deconstructs a zip file, encodes it in base64, and stores it in the database.

- **Parameters**: `zip_path` (str) - The path to the zip file.
- **Returns**: A tuple containing the receipt UID and status code.

#### `retrieve.Image(receiptUID)`

Retrieves an image from the database using the receipt UID.

- **Parameters**: `receiptUID` (str) - The unique identifier for the image.
- **Returns**: A tuple containing the image data and status code.

#### `retrieve.ZipFile(receiptUID)`

Retrieves a zip file from the database using the receipt UID.

- **Parameters**: `receiptUID` (str) - The unique identifier for the zip file.
- **Returns**: A tuple containing the zip file data and status code.

## Example Usage

Refer to the [basic_use.py](example/basic_use.py) file for an example of how to use the `PixelStorageOne` class.

```python
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
```

## Contributing

This is an open-source project, and contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License.

## Contact

For any questions or suggestions, please open an issue or contact the project maintainers.

## Donations

This project is intended to be open-source and free from cost to use. I love coding, setting a target and accomplishing it, sometimes by using pre-existing technology or creating an original approach to a problem. It excites me and gives me a sense of purpose, but it is not always easy to find the time or motivation to keep pushing forward. Donations are welcome if you wish to give something towards the work I do, but it is completely optional and is certainly not a requirement.

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/azio0)

