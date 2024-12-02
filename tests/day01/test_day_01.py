import os
import unittest

from parameterized import parameterized

from aoc2024.day01 import Day01


class TestDay01(unittest.TestCase):

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_01.txt"), 11),
            (os.path.join(ROOT_DIR, "../../input/Day01.txt"), 1320851),
        ]
    )
    def test_part_1(self, path, expected):
        result = Day01.part_1(path)

        self.assertEqual(expected, result)

    @parameterized.expand(
        [
            (os.path.join(ROOT_DIR, "test_day_01.txt"), 31),
            (os.path.join(ROOT_DIR, "../../input/Day01.txt"), 26859182),
        ]
    )
    def test_part_2(self, path, expected):
        result = Day01.part_2(path)

        self.assertEqual(expected, result)
