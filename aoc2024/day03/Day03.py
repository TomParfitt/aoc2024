import re


def part_1(path):
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

    with open(path) as file:
        lines = [line for line in file]

    total = 0
    for line in lines:
        matches = pattern.findall(line)

        for first, second in matches:
            total += int(first) * int(second)

    return total


def part_2(path):
    pattern = re.compile(r"(do\(\))|(don\'t\(\))|mul\((\d{1,3}),(\d{1,3})\)")

    with open(path) as file:
        lines = [line for line in file]

    do = True
    total = 0
    for line in lines:
        matches = pattern.findall(line)

        for match in matches:
            if (match[0]) == "do()":
                do = True
            elif (match[1]) == "don't()":
                do = False
            elif do:
                total += int(match[2]) * int(match[3])

    return total
