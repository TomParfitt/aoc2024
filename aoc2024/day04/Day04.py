def dfs(lines, word, prev_idx, prev_x, prev_y, direction):
    curr_y = prev_y + direction[1]
    curr_x = prev_x + direction[0]
    curr_idx = prev_idx + 1

    if curr_y < 0 or curr_y >= len(lines):
        # outside Y bounds
        return False

    if curr_x < 0 or curr_x >= len(lines[curr_y]):
        # outside X bounds
        return False

    if lines[curr_y][curr_x] != word[curr_idx]:
        # next letter not correct
        return False

    if len(word) - 1 == curr_idx:
        return True

    return dfs(lines, word, curr_idx, curr_x, curr_y, direction)


def part_1(path):
    with open(path) as file:
        lines = [line for line in file]

    total = 0

    word = "XMAS"

    directions = [
        [-1, -1],
        [0, -1],
        [1, -1],
        [-1, 0],
        [1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
    ]

    for curr_y, line in enumerate(lines):
        for curr_x, letter in enumerate(line):
            if letter == word[0]:
                for direction in directions:
                    found = dfs(lines, word, 0, curr_x, curr_y, direction)
                    if found:
                        total += 1

    return total


def part_2(path):
    with open(path) as file:
        lines = [line for line in file]

    total = 0

    for curr_y, line in enumerate(lines):
        for curr_x, letter in enumerate(line):
            if (
                curr_x < 1
                or curr_y < 1
                or curr_y >= len(lines) - 1
                or curr_x >= len(lines[curr_y]) - 1
            ):
                # needs to be within bounds
                continue

            if letter == "A":
                if (
                    (
                        lines[curr_y - 1][curr_x - 1] == "M"
                        and lines[curr_y + 1][curr_x + 1] == "S"
                    )
                    or (
                        lines[curr_y - 1][curr_x - 1] == "S"
                        and lines[curr_y + 1][curr_x + 1] == "M"
                    )
                ) and (
                    (
                        lines[curr_y - 1][curr_x + 1] == "M"
                        and lines[curr_y + 1][curr_x - 1] == "S"
                    )
                    or (
                        lines[curr_y - 1][curr_x + 1] == "S"
                        and lines[curr_y + 1][curr_x - 1] == "M"
                    )
                ):
                    total += 1

    return total
