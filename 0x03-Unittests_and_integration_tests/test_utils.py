#!/usr/bin/env python3
"""Unit tests for utils.access_nested_map function."""

import unittest
from utils import access_nested_map
from parameterized import parameterized

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
