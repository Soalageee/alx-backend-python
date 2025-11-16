#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map function."""

import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the access_nested_map function."""
        
    @parameterized.expand ([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(self, nested_map: dict, path: tuple, expected: any) -> None:
        """Test access_nested_map returns the correct value for a given path."""
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand ([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])

    def test_access_nested_map_exception(self, nested_map: dict, path: tuple, expected: str) -> None:
        """Test that access_nested_map raises KeyError for invalid paths with correct key message."""

        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(context.exception.args[0], expected)



class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function."""

    @parameterized.expand ([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])

    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """Test get_json returns the expected payload without making real HTTP calls."""

        with patch("requests.get") as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = test_payload

            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
    