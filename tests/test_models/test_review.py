#!/usr/bin/python3
"""
Unittests for Review.
"""
import unittest
import pycodestyle
import datetime
import models
from models.base_model import BaseModel
from models.review import Review


class ReviewTests(unittest.TestCase):
    """
    Review tests.
    """
    rw = Review()

    def testAttributes(self):
        """
        Test cases for the attributes.
        """
        self.rw.place_id = "Place.id"
        self.rw.user_id = "User.id"
        self.rw.text = "New Review"
        dict_am = self.rw.to_dict()

        self.assertEqual(self.rw.place_id, dict_am["place_id"])
        self.assertEqual(self.rw.user_id, dict_am["user_id"])
        self.assertEqual(self.rw.text, dict_am["text"])
        self.assertEqual("Review", dict_am["__class__"])

    def testInheritance(self):
        """
        Test cases verify is subclass of BaseModel
        """
        self.assertIsInstance(self.rw, BaseModel)
        self.assertTrue(hasattr(self.rw, 'id'))
        self.assertTrue(hasattr(self.rw, 'created_at'))
        self.assertTrue(hasattr(self.rw, 'updated_at'))

    def testTypeAttributes(self):
        """
        Test case for validate type for attributes.
        """
        self.assertIsInstance(self.rw.place_id, str)
        self.assertIsInstance(self.rw.user_id, str)
        self.assertIsInstance(self.rw.text, str)
        self.assertIsInstance(self.rw.id, str)
        self.assertIsInstance(self.rw.created_at, datetime.datetime)
        self.assertIsInstance(self.rw.updated_at, datetime.datetime)

    def testDateUpdate(self):
        """
        Test case for validate change update_at.
        """
        self.rw.text = "Update 1"
        self.rw.save()
        dict_1 = self.rw.to_dict()

        self.rw.text = "Update 2"
        self.rw.save()
        dict_2 = self.rw.to_dict()

        self.assertEqual(dict_1["id"], dict_2["id"])
        self.assertEqual(dict_1["created_at"], dict_2["created_at"])
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])
        self.assertNotEqual(dict_1["text"], dict_2["text"])


if __name__ == "__main__":
    unittest.main()
