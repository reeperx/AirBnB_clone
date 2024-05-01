#!/usr/bin/python3
from models.state import State
import unittest


class TestState(unittest.TestCase):
    """tests State class"""
    def test_city(self):
        """tests the state"""
        self.assertIsNotNone(State().name)
