#!/usr/bin/python3
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """tests City class"""
    def test_city(self):
        """tests the city"""
        self.assertIsNotNone(City().state_id)
        self.assertIsNotNone(City().name)
