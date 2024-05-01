#!/usr/bin/python3
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """tests City class"""
    def test_amenity(self):
        """tests amenities"""
        self.assertIsNotNone(Amenity().name)
