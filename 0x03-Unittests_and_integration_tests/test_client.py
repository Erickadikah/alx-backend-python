#!/usr/bin/env python3
"""Uniittest Testcase for Class GithubOrgClient
"""
from msilib.schema import SelfReg
from typing import Self
import unittest
from parameterized import parameterized
from unittest import mock
from client import GithubOrgClient
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, param
from utils import get_json
import requests


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
        """
        expected = 'www.example.com'
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("x")
            self.assertEqual(cli._public_repos_url, expected)
