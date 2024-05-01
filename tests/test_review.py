#!/usr/bin/python3
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """tests City class"""
    def test_review(self):
        """tests the city"""
        self.assertIsNotNone(Review().place_id)
        self.assertIsNotNone(Review().user_id)
        self.assertIsNotNone(Review().text)
