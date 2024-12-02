def sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0


def check_line(line):
    prev_sign = 0
    for idx in range(1, len(line)):
        prev = line[idx-1]
        curr = line[idx]
        delta = curr - prev

        curr_sign = sign(delta)

        # if different direction
        if prev_sign and curr_sign != prev_sign:
            return False
        prev_sign = curr_sign

        # not greater than 1 but less than 4 diff
        if not 0 < abs(delta) < 4:
            return False

    return True


def part_1(path):
    with open(path, 'r') as file:
        lines = [line.split() for line in file]

    safe = 0
    for line in lines:
        num_safe_line = [int(x) for x in line]
        if check_line(num_safe_line):
            safe += 1

    return safe


def part_2(path):
    with open(path, 'r') as file:
        lines = [line.split() for line in file]

    safe = 0
    for line in lines:
        num_safe_line = [int(x) for x in line]
        if check_line(num_safe_line):
            safe += 1
        else:
            for idx in range(len(num_safe_line)):
                if check_line(num_safe_line[:idx] + num_safe_line[idx+1:]):
                    safe += 1
                    break

    return safe
