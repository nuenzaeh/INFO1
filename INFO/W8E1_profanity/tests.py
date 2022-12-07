#!/usr/bin/env python3

from unittest import TestCase
from main import ProfanityFilter


class PublicTestSuite(TestCase):

    def test_example(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        msg = "abc defghi mastard jklmno"
        actual = f.filter(msg)
        expected = "abc defghi ?#$?#$? jklmno"
        self.assertEqual(expected, actual)

    def test_contained(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        offensive_msg = "abc defghi mastard jklmno enbatching"
        actual = f.filter(offensive_msg)
        expected = "abc defghi ?#$?#$? jklmno en?#$?#ing"
        self.assertEqual(expected, actual)

    def test_uppercase(self):
        f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
        offensive_msg = "abc defghi MasTard jklmno enBatching"
        actual = f.filter(offensive_msg)
        expected = "abc defghi ?#$?#$? jklmno en?#$?#ing"
        self.assertEqual(expected, actual)
    # This current test suite only contains one very basic test case. By now,
    # you have some experience in writing test cases. We strongly ecncourage
    # you to implement further test cases. The additional tests can be run via
    # 'Test&Run' in ACCESS. These tests won't affect the grading of your solution
    # directly, but they can help you with identifying relevant corner cases
    # that you have to consider in your implementation.
