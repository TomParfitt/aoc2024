import os
import unittest

from parameterized import parameterized

from aoc2024.day05 import day_05


class TestDay05(unittest.TestCase):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_05.txt"), 143),
            (os.path.join(ROOT_DIR, "../../input/day_05.txt"), 5208),
        ]
    )
    def test_part_1(self, path, expected):
        result = day_05.part_1(path)
        self.assertEqual(expected, result)

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_05.txt"), 123),
            (os.path.join(ROOT_DIR, "../../input/day_05.txt"), 6732),
        ]
    )
    def test_part_2(self, path, expected):
        result = day_05.part_2(path)
        self.assertEqual(expected, result)
