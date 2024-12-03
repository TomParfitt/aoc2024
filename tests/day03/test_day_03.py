import os
import unittest

from parameterized import parameterized

from aoc2024.day03 import Day03


class TestDay03(unittest.TestCase):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_03_1.txt"), 161),
            (os.path.join(ROOT_DIR, "../../input/day_03.txt"), 187833789),
        ]
    )
    def test_part_1(self, path, expected):
        result = Day03.part_1(path)
        self.assertEqual(expected, result)

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_03_2.txt"), 48),
            (os.path.join(ROOT_DIR, "../../input/day_03.txt"), 94455185),
        ]
    )
    def test_part_2(self, path, expected):
        result = Day03.part_2(path)
        self.assertEqual(expected, result)
