#!/usr/bin/python3
"""registers objects to memory by creating an instance read from JSON file"""


from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
