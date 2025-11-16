#!/usr/bin/env python3

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient method"""
    
    @parameterized.expand ([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])

    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """Test that GithubOrgClient.org returns the expected payload"""
        
        mock_get_json.return_value = expected_payload
        client = GithubOrgClient(org_name)

        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

        self.assertEqual(result, expected_payload)


    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected URL"""
        
        payload = {"repos_url": "https://api.github.com/orgs/testorg/repos"}

        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload

            client = GithubOrgClient("testorg")
            result = client._public_repos_url

            expected = "https://api.github.com/orgs/testorg/repos"
            self.assertEqual(result, expected)
