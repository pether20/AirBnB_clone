#!/usr/bin/python3
"""
Unittests for Amenity.
"""
import unittest
import pycodestyle
import datetime
import models
from models.base_model import BaseModel
from models.amenity import Amenity


class AmenityTests(unittest.TestCase):
    """
    Amenity tests.
    """
    am = Amenity()

    def testAttributes(self):
        """
        Test cases for the attributes.
        """
        self.am.name = "New Amenity"
        dict_am = self.am.to_dict()

        self.assertEqual(self.am.name, dict_am["name"])
        self.assertEqual("Amenity", dict_am["__class__"])

    def testInheritance(self):
        """
        Test cases verify is subclass of BaseModel
        """
        self.assertIsInstance(self.am, BaseModel)
        self.assertTrue(hasattr(self.am, 'id'))
        self.assertTrue(hasattr(self.am, 'created_at'))
        self.assertTrue(hasattr(self.am, 'updated_at'))

    def testTypeAttributes(self):
        """
        Test case for validate type for attributes.
        """
        self.assertIsInstance(self.am.name, str)
        self.assertIsInstance(self.am.id, str)
        self.assertIsInstance(self.am.created_at, datetime.datetime)
        self.assertIsInstance(self.am.updated_at, datetime.datetime)

    def testDateUpdate(self):
        """
        Test case for validate change update_at.
        """
        self.am.name = "Update 1"
        self.am.save()
        dict_1 = self.am.to_dict()

        self.am.name = "Update 2"
        self.am.save()
        dict_2 = self.am.to_dict()

        self.assertEqual(dict_1["id"], dict_2["id"])
        self.assertEqual(dict_1["created_at"], dict_2["created_at"])
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])
        self.assertNotEqual(dict_1["name"], dict_2["name"])


if __name__ == "__main__":
    unittest.main()
