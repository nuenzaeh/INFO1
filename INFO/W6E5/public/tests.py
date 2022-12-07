#!/usr/bin/env python3

from unittest import TestCase
from script import analyze

# This test suite does not exhaustively test the implementation,
# a passing "test & run" does not mean that all possible cases
# have been considered. For the grading, an extended tests suite
# will be executed that will cover many more cases.

# Feel free to add additional test cases here. All test cases
# will be executed as part of the "Test & Run".


class PublicTestSuite(TestCase):

    def test_1(self):
        actual = analyze(["hi #weekend",
                          "good morning #zurich #limmat",
                          "spend my #weekend in #zurich",
                          "#zurich <3"])
        expected = {'weekend': 2, 'zurich': 3, 'limmat': 1}
        self.assertEqual(expected, actual)
    
    def test_2(self):
        actual = analyze(["",
                          "good morning #90zurich #limmat",
                          "spend my #weekend in #zurich",
                          "#Zurich <3"])
        expected = {'limmat': 1, 'weekens': 1, 'zurich': 7, 'Zurich': 1}
        self.assertEqual(expected, actual)
