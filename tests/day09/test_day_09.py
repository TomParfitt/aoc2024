import os
import unittest

from parameterized import parameterized

from aoc2024.day09 import day_09


class TestDay09(unittest.TestCase):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_09.txt"), 1928),
            (os.path.join(ROOT_DIR, "../../input/day_09.txt"), 6258319840548),
        ]
    )
    def test_part_1(self, path, expected):
        result = day_09.part_1(path)
        self.assertEqual(expected, result)

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_09.txt"), 2858),
            (os.path.join(ROOT_DIR, "../../input/day_09.txt"), 6286182965311),
        ]
    )
    def test_part_2(self, path, expected):
        result = day_09.part_2(path)
        self.assertEqual(expected, result)
