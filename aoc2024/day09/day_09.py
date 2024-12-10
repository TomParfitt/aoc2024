def part_1(path):
    with open(path) as file:
        line = file.read().rstrip()

    file_id = 0
    file_system = []

    for i in range(0, len(line), 2):
        file_blocks = int(line[i])
        file_space = int(line[i + 1]) if i + 1 < len(line) else 0

        file_system.extend([file_id] * file_blocks)
        file_system.extend("." * file_space)

        file_id += 1

    space_index = 0
    for block_idx, block in reversed(list(enumerate(file_system))):
        if block != ".":

            while space_index < block_idx:
                space_index += 1
                if file_system[space_index] == ".":
                    file_system[space_index] = file_system[block_idx]
                    file_system[block_idx] = "."
                    break
            else:
                break

    total = 0
    for block_idx, block in enumerate(file_system):
        if block != ".":
            total += block_idx * block

    return total


def part_2(path):
    with open(path) as file:
        line = file.read().rstrip()

    file_id = 0
    file_system = []

    for i in range(0, len(line), 2):
        file_blocks = int(line[i])
        file_space = int(line[i + 1]) if i + 1 < len(line) else 0

        file_system.extend([file_id] * file_blocks)
        file_system.extend(["."] * file_space)

        file_id += 1

    block_index = len(file_system) - 1
    while block_index > 0:
        if file_system[block_index] != ".":
            count = 1
            block_id = file_system[block_index]

            # how many blocks are we moving
            while block_index - 1 > 0 and file_system[block_index - 1] == block_id:
                count += 1
                block_index -= 1

            # find the next space that will fit it
            swap_next_available(block_id, block_index, count, file_system)

        block_index -= 1

    print(file_system)

    total = 0
    for block_idx, block in enumerate(file_system):
        if block != ".":
            total += block_idx * block

    return total


def swap_next_available(block_id, block_index, count, file_system):
    space_count = 0
    for idx in range(len(file_system)):

        if idx > block_index:
            break

        if file_system[idx] == ".":
            space_count += 1
            if space_count == count:
                # swap them
                for i in range(idx - count + 1, idx + 1):
                    file_system[i] = block_id
                for i in range(block_index, block_index + count):
                    file_system[i] = "."
                break
        else:
            space_count = 0
