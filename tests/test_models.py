#!/usr/bin/pyrhon3
"""python unittest for BaseModel class"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestModel(unittest.TestCase):
    """testing model"""

    def setUp(self):
        """set up test"""
        self.inst = BaseModel()
        self.id = self.inst.id
        self.created_at = self.inst.created_at

    def test_save(self):
        """tests model save status"""
        model = BaseModel()
        model.save()
        self.assertIsNotNone(model.updated_at)
        self.assertIsInstance(model.updated_at, datetime)

    def test_to_dict(self):
        """tests to_dict return value"""
        kw = {'name': 'Dami'}
        self.assertEqual(BaseModel().to_dict()['__class__'], 'BaseModel')
        self.assertIsInstance(BaseModel().to_dict(), dict)
        self.assertIsNotNone(BaseModel(kw).to_dict())

    def test_id(self):
        """tests BaseModel id"""
        self.assertIsInstance(self.id, str)
        self.assertIsNotNone(self.id)
        self.assertNotEqual(self.id, '')

    def test_created_at(self):
        """tests value of created_at"""
        self.assertIsNotNone(self.created_at)
        self.assertIsInstance(self.created_at, datetime)

    def test_str(self):
        """checks the __str__ return for base_model"""
        self.assertIsInstance(str(BaseModel()), str)
        self.assertNotEqual(str(BaseModel()), '')
