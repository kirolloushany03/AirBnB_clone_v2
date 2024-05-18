#!/usr/bin/python3

"""script to test db storage"""
from models import DBStorage


import unittest
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "test not relevant")
class TestDB(unittest.TestCase):
    """assert documentation"""

    def test_doc(self):
        """assert doc of dbstorage"""
        self.assertIsNotNone(DBStorage.__doc__)
