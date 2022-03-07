#!/usr/bin/python3
"""
Unittests for User.
"""
import unittest
import pycodestyle
import datetime
import models
from models.base_model import BaseModel
from models.user import User


class UserTests(unittest.TestCase):
    """
    User tests.
    """
    us = User()

    def testAttributes(self):
        """
        Test cases for the attributes.
        """
        self.us.email = "email@gmail.com"
        self.us.password = "password"
        self.us.first_name = "First Name"
        self.us.last_name = "Last Name"
        dict_am = self.us.to_dict()

        self.assertEqual(self.us.email, dict_am["email"])
        self.assertEqual(self.us.password, dict_am["password"])
        self.assertEqual(self.us.first_name, dict_am["first_name"])
        self.assertEqual(self.us.last_name, dict_am["last_name"])
        self.assertEqual("User", dict_am["__class__"])

    def testInheritance(self):
        """
        Test cases verify is subclass of BaseModel
        """
        self.assertIsInstance(self.us, BaseModel)
        self.assertTrue(hasattr(self.us, 'id'))
        self.assertTrue(hasattr(self.us, 'created_at'))
        self.assertTrue(hasattr(self.us, 'updated_at'))

    def testTypeAttributes(self):
        """
        Test case for validate type for attributes.
        """
        self.assertIsInstance(self.us.email, str)
        self.assertIsInstance(self.us.password, str)
        self.assertIsInstance(self.us.first_name, str)
        self.assertIsInstance(self.us.last_name, str)
        self.assertIsInstance(self.us.id, str)
        self.assertIsInstance(self.us.created_at, datetime.datetime)
        self.assertIsInstance(self.us.updated_at, datetime.datetime)

    def testDateUpdate(self):
        """
        Test case for validate change update_at.
        """
        self.us.first_name = "Update 1"
        self.us.save()
        dict_1 = self.us.to_dict()

        self.us.first_name = "Update 2"
        self.us.save()
        dict_2 = self.us.to_dict()

        self.assertEqual(dict_1["id"], dict_2["id"])
        self.assertEqual(dict_1["created_at"], dict_2["created_at"])
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])
        self.assertNotEqual(dict_1["first_name"], dict_2["first_name"])


if __name__ == "__main__":
    unittest.main()
