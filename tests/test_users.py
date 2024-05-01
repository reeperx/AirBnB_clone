#!/usr/bin/python3
"""python unnitest for user class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """test class User attributes"""
    def test_firstname(self):
        """test first name"""
        self.assertIsNotNone(User().first_name)
        self.assertIsInstance(User().first_name, str)

    def test_lastname(self):
        """tests laatname"""
        self.assertIsNotNone(User().last_name)
        self.assertIsInstance(User().last_name, str)

    def test_email(self):
        """tests email"""
        self.assertIsNotNone(User().email)
        self.assertIsInstance(User().email, str)

    def test_password(self):
        """tests password"""
        self.assertIsNotNone(User().password)
        self.assertIsInstance(User().password, str)
