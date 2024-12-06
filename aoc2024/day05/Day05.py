import math
from functools import cmp_to_key


def compare(map_order, item1, item2):
    if item1 in map_order:
        if item2 in map_order[item1]:
            return -1
        else:
            return 1
    else:
        return 0


def part_1(path):
    page_map = {}
    lines = []

    with open(path) as file:
        for line in file:
            if "|" in line:
                before, after = line.rstrip().split("|")
                if before not in page_map:
                    page_map[before] = {after}
                else:
                    page_map[before].add(after)
            elif "," in line:
                lines.append(line)

    total = 0

    for line in lines:
        pages = line.rstrip().split(",")
        pages_in_order = sorted(
            pages, key=cmp_to_key(lambda item1, item2: compare(page_map, item1, item2))
        )

        if pages == pages_in_order:
            half_way = math.floor(len(pages) / 2)
            total += int(pages[half_way])

    return total


def part_2(path):
    page_map = {}
    lines = []

    with open(path) as file:
        for line in file:
            if "|" in line:
                before, after = line.rstrip().split("|")
                if before not in page_map:
                    page_map[before] = {after}
                else:
                    page_map[before].add(after)
            elif "," in line:
                lines.append(line)

    total = 0

    for line in lines:
        pages = line.rstrip().split(",")
        pages_in_order = sorted(
            pages, key=cmp_to_key(lambda item1, item2: compare(page_map, item1, item2))
        )

        if pages != pages_in_order:
            half_way = math.floor(len(pages_in_order) / 2)
            total += int(pages_in_order[half_way])

    return total
