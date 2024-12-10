directions = [
    [0, -1],  # above
    [-1, 0],  # left
    [1, 0],  # right
    [0, 1],  # below
]


def count_nines_reachable(lines, looking_for, prev_y_index, prev_x_index):
    indexes = []
    for direction in directions:
        curr_y = prev_y_index + direction[1]
        curr_x = prev_x_index + direction[0]

        if curr_y < 0 or curr_y >= len(lines):
            # outside Y bounds
            continue

        if curr_x < 0 or curr_x >= len(lines[curr_y]):
            # outside X bounds
            continue

        if lines[curr_y][curr_x] != str(looking_for):
            # next letter not correct
            continue

        if looking_for == 9:
            indexes.append((curr_y, curr_x))
        else:
            indexes.extend(
                count_nines_reachable(lines, looking_for + 1, curr_y, curr_x)
            )

    return indexes


def part_1(path):

    with open(path) as file:
        lines = [line for line in file]

    total = 0
    for y_index, line in enumerate(lines):
        for x_index, num in enumerate(line):
            if num == "0":
                indexes = count_nines_reachable(lines, 1, y_index, x_index)
                unique_indexes = set(indexes)
                total += len(unique_indexes)

    return total


def part_2(path):
    with open(path) as file:
        lines = [line for line in file]

    total = 0
    for y_index, line in enumerate(lines):
        for x_index, num in enumerate(line):
            if num == "0":
                indexes = count_nines_reachable(lines, 1, y_index, x_index)
                total += len(indexes)

    return total
