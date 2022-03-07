#!/usr/bin/python3
""" subclass State """
from models.base_model import BaseModel


class Place(BaseModel):
    """ class places"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
