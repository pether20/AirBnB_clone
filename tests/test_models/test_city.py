#!/usr/bin/python3
"""
Unittests for City.
"""
import unittest
import pycodestyle
import datetime
import models
from models.base_model import BaseModel
from models.city import City

class CityTests(unittest.TestCase):
    """
    City tests.
    """
    ct = City()

    def testAttributes(self):
        """
        Test cases for the attributes.
        """
        self.ct.name = "New City"
        self.ct.state_id = "State.id"
        dict_am = self.ct.to_dict()

        self.assertEqual(self.ct.name, dict_am["name"])
        self.assertEqual(self.ct.state_id, dict_am["state_id"])
        self.assertEqual("City", dict_am["__class__"])

    def testInheritance(self):
        """
        Test cases verify is subclass of BaseModel
        """
        self.assertIsInstance(self.ct, BaseModel)
        self.assertTrue(hasattr(self.ct, 'id'))
        self.assertTrue(hasattr(self.ct, 'created_at'))
        self.assertTrue(hasattr(self.ct, 'updated_at'))

    def testTypeAttributes(self):
        """
        Test case for validate type for attributes.
        """
        self.assertIsInstance(self.ct.name, str)
        self.assertIsInstance(self.ct.state_id, str)
        self.assertIsInstance(self.ct.id, str)
        self.assertIsInstance(self.ct.created_at, datetime.datetime)
        self.assertIsInstance(self.ct.updated_at, datetime.datetime)

    def testDateUpdate(self):
        """
        Test case for validate change update_at.
        """
        self.ct.name = "Update 1"
        self.ct.save()
        dict_1 = self.ct.to_dict()

        self.ct.name = "Update 2"
        self.ct.save()
        dict_2 = self.ct.to_dict()

        self.assertEqual(dict_1["id"], dict_2["id"])
        self.assertEqual(dict_1["created_at"], dict_2["created_at"])
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])
        self.assertNotEqual(dict_1["name"], dict_2["name"])


if __name__ == "__main__":
    unittest.main()
