#!/usr/bin/python3
"""
Unittests for State.
"""
import unittest
import pycodestyle
import datetime
import models
from models.base_model import BaseModel
from models.state import State


class StateTests(unittest.TestCase):
    """
    State tests.
    """
    st = State()

    def testAttributes(self):
        """
        Test cases for the attributes.
        """
        self.st.name = "New State"
        dict_am = self.st.to_dict()

        self.assertEqual(self.st.name, dict_am["name"])
        self.assertEqual("State", dict_am["__class__"])

    def testInheritance(self):
        """
        Test cases verify is subclass of BaseModel
        """
        self.assertIsInstance(self.st, BaseModel)
        self.assertTrue(hasattr(self.st, 'id'))
        self.assertTrue(hasattr(self.st, 'created_at'))
        self.assertTrue(hasattr(self.st, 'updated_at'))

    def testTypeAttributes(self):
        """
        Test case for validate type for attributes.
        """
        self.assertIsInstance(self.st.name, str)
        self.assertIsInstance(self.st.id, str)
        self.assertIsInstance(self.st.created_at, datetime.datetime)
        self.assertIsInstance(self.st.updated_at, datetime.datetime)

    def testDateUpdate(self):
        """
        Test case for validate change update_at.
        """
        self.st.name = "Update 1"
        self.st.save()
        dict_1 = self.st.to_dict()

        self.st.name = "Update 2"
        self.st.save()
        dict_2 = self.st.to_dict()

        self.assertEqual(dict_1["id"], dict_2["id"])
        self.assertEqual(dict_1["created_at"], dict_2["created_at"])
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])
        self.assertNotEqual(dict_1["name"], dict_2["name"])


if __name__ == "__main__":
    unittest.main()
