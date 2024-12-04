import os
import unittest

from parameterized import parameterized

from aoc2024.day04 import Day04


class TestDay04(unittest.TestCase):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_04_1.txt"), 4),
            (os.path.join(ROOT_DIR, "test_day_04_2.txt"), 18),
            (os.path.join(ROOT_DIR, "test_day_04_3.txt"), 18),
            (os.path.join(ROOT_DIR, "../../input/day_04.txt"), 2434),
        ]
    )
    def test_part_1(self, path, expected):
        result = Day04.part_1(path)
        self.assertEqual(expected, result)

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_04_4.txt"), 1),
            (os.path.join(ROOT_DIR, "test_day_04_5.txt"), 9),
            (os.path.join(ROOT_DIR, "../../input/day_04.txt"), 1835),
        ]
    )
    def test_part_2(self, path, expected):
        result = Day04.part_2(path)
        self.assertEqual(expected, result)
