import os
import unittest

from parameterized import parameterized

from aoc2024.day10 import day_10


class TestDay09(unittest.TestCase):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_10_1.txt"), 1),
            (os.path.join(ROOT_DIR, "test_day_10_2.txt"), 36),
            (os.path.join(ROOT_DIR, "../../input/day_10.txt"), 717),
        ]
    )
    def test_part_1(self, path, expected):
        result = day_10.part_1(path)
        self.assertEqual(expected, result)

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_10_2.txt"), 81),
            (os.path.join(ROOT_DIR, "../../input/day_10.txt"), 1686),
        ]
    )
    def test_part_2(self, path, expected):
        result = day_10.part_2(path)
        self.assertEqual(expected, result)
