#!/usr/bin/env python3
"""Uniittest Testcase for Class
"""

import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from unittest import expectedFailure, mock


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
        expected = 'www.holberton.io'
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("y")
            self.assertEqual(cli._public_repos_url, expected)

    @parameterized.expand([
        ({'license': {'key': "GNU PL"}}, "GNU PL", True),
        ({'license': {'key': "MIT-5.0"}}, "GNU PL", False),
    ])
    def test_has_license(self, repo: dict, key: str, expected: bool) -> None:
        """Args: repo, key,
            expected
            Return: None
        """
        client = GithubOrgClient("google")
        permit = client.has_license(repo, key)
        self.assertEqual(permit, expected)

    # @parameterized.expand([
    #     ({"license": {"key": "my_license"}}, "my_license", True),
    #     ({"license": {"key": "other_license"}}, "other_license", True)
    # ])
    # def test_has_license(self, repo, license, expected):
    #     """Test case
    #     """

    #     GithubOrgClient1 = GithubOrgClient('google')
    #     Client1 = GithubOrgClient1.has_license(repo,license)
    #     self.assertEqual(Client1(expected))

    @paramaterized.expand([
        ('org_payload', 'repos_payload', 'expected_repos', ' apache2_repos')
    ])
class GithubOrgClient(unittest.TestCase):
    """Intergration testcase
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass
