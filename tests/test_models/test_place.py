#!/usr/bin/python3
"""
Unittests for Place.
"""
import unittest
import pycodestyle
import datetime
import models
from models.base_model import BaseModel
from models.place import Place


class PlaceTests(unittest.TestCase):
    """
    Place tests.
    """
    pc = Place()

    def testAttributes(self):
        """
        Test cases for the attributes.
        """
        self.pc.city_id = "City.id"
        self.pc.user_id = "User.id"
        self.pc.name = "New Place"
        self.pc.description = "Description"
        self.pc.number_rooms = 1
        self.pc.number_bathrooms = 1
        self.pc.max_guest = 1
        self.pc.price_by_night = 10
        self.pc.latitude = 10.1
        self.pc.longitude = 11.2
        self.pc.amenity_ids = ["Amenity 1", "Amenity 2"]

        dict_am = self.pc.to_dict()

        self.assertEqual(self.pc.city_id, dict_am["city_id"])
        self.assertEqual(self.pc.user_id, dict_am["user_id"])
        self.assertEqual(self.pc.name, dict_am["name"])
        self.assertEqual(self.pc.description, dict_am["description"])
        self.assertEqual(self.pc.number_rooms, dict_am["number_rooms"])
        self.assertEqual(self.pc.number_bathrooms, dict_am["number_bathrooms"])
        self.assertEqual(self.pc.max_guest, dict_am["max_guest"])
        self.assertEqual(self.pc.price_by_night, dict_am["price_by_night"])
        self.assertEqual(self.pc.latitude, dict_am["latitude"])
        self.assertEqual(self.pc.longitude, dict_am["longitude"])
        self.assertEqual(self.pc.amenity_ids, dict_am["amenity_ids"])
        self.assertEqual("Place", dict_am["__class__"])

    def testInheritance(self):
        """
        Test cases verify is subclass of BaseModel
        """
        self.assertIsInstance(self.pc, BaseModel)
        self.assertTrue(hasattr(self.pc, 'id'))
        self.assertTrue(hasattr(self.pc, 'created_at'))
        self.assertTrue(hasattr(self.pc, 'updated_at'))

    def testTypeAttributes(self):
        """
        Test case for validate type for attributes.
        """
        self.assertIsInstance(self.pc.city_id, str)
        self.assertIsInstance(self.pc.user_id, str)
        self.assertIsInstance(self.pc.name, str)
        self.assertIsInstance(self.pc.description, str)
        self.assertIsInstance(self.pc.number_rooms, int)
        self.assertIsInstance(self.pc.number_bathrooms, int)
        self.assertIsInstance(self.pc.max_guest, int)
        self.assertIsInstance(self.pc.price_by_night, int)
        self.assertIsInstance(self.pc.latitude, float)
        self.assertIsInstance(self.pc.longitude, float)
        self.assertIsInstance(self.pc.amenity_ids, list)
        self.assertIsInstance(self.pc.created_at, datetime.datetime)
        self.assertIsInstance(self.pc.updated_at, datetime.datetime)

    def testDateUpdate(self):
        """
        Test case for validate change update_at.
        """
        self.pc.name = "Update 1"
        self.pc.save()
        dict_1 = self.pc.to_dict()

        self.pc.name = "Update 2"
        self.pc.save()
        dict_2 = self.pc.to_dict()

        self.assertEqual(dict_1["id"], dict_2["id"])
        self.assertEqual(dict_1["created_at"], dict_2["created_at"])
        self.assertNotEqual(dict_1["updated_at"], dict_2["updated_at"])
        self.assertNotEqual(dict_1["name"], dict_2["name"])


if __name__ == "__main__":
    unittest.main()
