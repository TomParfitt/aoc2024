import unittest

from parameterized import parameterized

from aoc2024.Day02 import Day02


class Day02Test(unittest.TestCase):

    @parameterized.expand(
        [
            ("Day02Test.txt", 2),
            ("../../input/Day02.txt", 299),
        ]
    )
    def test_part_1(self, path, expected):
        result = Day02.part_1(path)
        self.assertEqual(expected, result)

    @parameterized.expand(
        [
            ("Day02Test.txt", 4),
            ("../../input/Day02.txt", 364),
        ]
    )
    def test_part_2(self, path, expected):
        result = Day02.part_2(path)
        self.assertEqual(expected, result)
