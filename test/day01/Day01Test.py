import unittest

from parameterized import parameterized
from aoc2024.day01 import Day01


class Day01Test(unittest.TestCase):

    @parameterized.expand([
        ('Day01Test.txt', 11),
        ('../../input/Day01.txt', 1320851),
    ])
    def test_part_1(self, path, expected):
        result = Day01.part_1(path)

        self.assertEqual(expected, result)

    @parameterized.expand([
        ('Day01Test.txt', 31),
        ('../../input/Day01.txt', 26859182),
    ])
    def test_part_2(self, path, expected):
        result = Day01.part_2(path)

        self.assertEqual(expected, result)
