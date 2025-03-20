from utils.config.worker import *
from utils.database.worker import *
from utils.database.queries import *
from utils.pillow.worker import *
from utils.transaction.worker import *
from utils.ziparchive.worker import *

if __name__ == "__main__":
    create_image_table()
    create_zip_table()
