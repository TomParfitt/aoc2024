def part_1(path):
    with open(path) as file:
        lines = [line.split() for line in file]

    team1 = []
    team2 = []
    for col1, col2 in lines:
        team1.append(int(col1))
        team2.append(int(col2))

    team1_sorted = sorted(team1)
    team2_sorted = sorted(team2)

    total_distance = 0
    for index in range(len(team1_sorted)):
        distance = team1_sorted[index] - team2_sorted[index]
        total_distance += abs(distance)

    return total_distance


def part_2(path):
    with open(path) as file:
        lines = [line.split() for line in file]

    team1 = []
    team2 = {}
    for col1, col2 in lines:
        team1.append(col1)
        team2[col2] = team2.get(col2, 0) + int(col2)

    similarity = 0
    for col1 in team1:
        similarity += team2.get(col1, 0)

    return similarity
