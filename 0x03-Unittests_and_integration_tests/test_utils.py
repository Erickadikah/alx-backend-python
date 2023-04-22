#!/usr/bin/env python3
"""unittest Module for testing nested map access
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, memoize
import requests
from unittest import mock
import functools


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


class TestGetJson(unittest.TestCase):
    """Method to test utils.get_json return expected output
        using mock.patch to patch requests.get
        Reaturns: a mock object
    """

    def test_get_json(self):
        """
        Test that the utils.get_json function returns the expected output.
        Returns: test_payload = {'key': 'value'}
        test_url = "http://example.com"
        response = requests.get(test_url)
        return response.json()
        """
        test_payload = {'key': 'value'}
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            response = requests.get('http://example.com')
            data = response.json()
            self.assertEqual(data, test_payload)


class TestMemoize(unittest.TestCase):
    """Tsting if function memoize is being called one
    """

    def memoize(func):
        """memoize func
        """
        return functools.lru_cache()(func)

    def test_memoize(self):
        """test
        """
        class TestClass:
            """Class test for the return value 42
            """

            def a_method(self):
                return 42

        @memoize
        def a_property(self, arg):
            return self.a_method() + arg
