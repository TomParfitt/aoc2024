import os
import unittest

from parameterized import parameterized

from aoc2024.Day02 import Day02


class TestDay02(unittest.TestCase):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_02.txt"), 2),
            (os.path.join(ROOT_DIR, "../../input/Day02.txt"), 299),
        ]
    )
    def test_part_1(self, path, expected):
        result = Day02.part_1(path)
        self.assertEqual(expected, result)

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_02.txt"), 4),
            (os.path.join(ROOT_DIR, "../../input/Day02.txt"), 364),
        ]
    )
    def test_part_2(self, path, expected):
        result = Day02.part_2(path)
        self.assertEqual(expected, result)
