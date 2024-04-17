#!/usr/bin/python3
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


# Determine the storage type based on the environment variable
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
