#!/usr/bin/python3
"""Test BaseModel- Comproving expectect outputs and documentation"""
from datetime import datetime
import time
import unittest
# from pep8 import pycodestyle
import models
import inspect
from unittest import mock

BaseModel = models.base_model.BaseModel
mod_doc = models.base_model.__doc__


class TestDocs(unittest.TestCase):
    """Test documentation and style"""
    @classmethod
    def setUpClass(self):
        """Setup for dosctring"""
        self.base_f = inspect.getmembers(BaseModel, inspect.isfunction)

    # def testing_pep8(self):
    # """testing that BaseModel.py passes pep8"""
    # for path in ['models/base_model.py',
    # "tests/test_models/test_base_model.py"]:
    # with self.suptest(path=path):
    # err = pycodestyle.Checker(path).check_all()
    # self.assertEqual(err, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(mod_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(mod_doc) > 1,
                        "base_model.py needs a docstring")

    def test_dosctring(self):
        """Testing documentation"""
        self.assertIsNot(mod_doc, None,
                         "base_model.py needs a doctring")
        self.assertTrue(len(mod_doc) > 1,
                        "base_model.py needs a docstring")


if __name__ == '__main__':
    unittest.main
