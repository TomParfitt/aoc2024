import unittest


class Day01Test(unittest.TestCase):

    def test_day_01_part1(self):
        with open('Day01Test.txt', 'r') as file:
            lines = [line.split() for line in file]

        team1 = []
        team2 = []
        for col1, col2 in lines:
            team1.append(int(col1))
            team2.append(int(col2))

        team1_sorted = sorted(team1)
        team2_sorted = sorted(team2)

        differences = []
        for index in range(len(team1_sorted)):
            difference = team1_sorted[index] - team2_sorted[index]
            differences.append(abs(difference))

        self.assertEqual(1320851, sum(differences))

    def test_day_01_part2(self):
        with open('Day01Test.txt', 'r') as file:
            lines = [line.split() for line in file]

        team1 = []
        team2 = {}
        for col1, col2 in lines:
            team1.append(col1)
            team2[col2] = team2.get(col2, 0) + int(col2)

        similarity = 0
        for col1 in team1:
            similarity += team2.get(col1, 0)

        self.assertEqual(26859182, similarity)
