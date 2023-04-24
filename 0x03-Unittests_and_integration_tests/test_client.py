#!/usr/bin/env python3
"""Uniittest Testcase for Class
"""

import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
import utils
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
import client
from fixtures import TEST_PAYLOAD
from unittest import mock


class TestGithubOrgClient(unittest.TestCase):
    """GithubOrClient test
    """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """Function to test org if its is returning the correct  values
        """
        get_patch.return_value = expected
        y = GithubOrgClient(org)
        self.assertEqual(y.org, expected)
        get_patch.assert_called_once_with('https://api.github.com/orgs/' + org)

    def test_public_repos_url(self):
        """expected one based on the mocked payload.
            Cli : GithubOrgClient
        """
        expected = 'https://api.github.com/orgs/testorg/repos'
        payload = {"repos_url": expected}
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = payload
            cli = GithubOrgClient("testorg")
            self.assertEqual(cli._public_repos_url, expected)
