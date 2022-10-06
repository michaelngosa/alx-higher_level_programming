#!/usr/bin/python3
""" Defines unittest for Base class """

from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square


class Test_base_instantiation(unittest.TestCase):
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id -1)

    def test_none_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id -1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_string_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_dict_id(self):
        self.assertEqual({"a":1, "b":2}, Base({"a":1, "b":2}).id)

    def test_list_id(self):
        self.asserEqual([1,2,3], Base([1,2,3]).id)

    def test_two_arg(self):
        with self.assertRaises(TypeError):
            Base(1,3)
