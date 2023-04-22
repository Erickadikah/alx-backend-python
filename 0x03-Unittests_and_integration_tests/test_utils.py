#!/usr/bin/env python3
"""unittest Module for testing nested map access
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Class Nested map for tests
    """
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, base, exponent, expected):
        """
        Test access_nested_map
        """
        self.assertEqual(access_nested_map(base, exponent), expected)

    @parameterized.expand([
        ({}, ["a"]),
        ({"a": 1}, ["a", "b"])
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map exception
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)
