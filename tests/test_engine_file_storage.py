#!/usr/bin/python3
from models.engine.file_storage import FileStorage as Storage
import unittest


class TestStorage(unittest.TestCase):
    """tests City class"""
    def test_file_storage(self):
        """tests the city"""
        self.assertIsInstance(Storage().all(), dict)
