import re
import copy


def part_1(d, h, w, s):
    q1 = q2 = q3 = q4 = 0

    x0, y0 = h // 2, w // 2

    for r in d:
        r[0] = (r[0] + s * r[2]) % w
        r[1] = (r[1] + s * r[3]) % h

        if r[0] > y0:
            if r[1] < x0:
                q1 += 1
            elif r[1] > x0:
                q2 += 1
        elif r[0] < y0:
            if r[1] > x0:
                q3 += 1
            elif r[1] < x0:
                q4 += 1

    return q1 * q2 * q3 * q4


def part_2(d, h, w):
    s = 0
    no_tree = True

    while no_tree:
        s += 1
        rows, cols = {}, {}

        for r in d:
            r[0] = (r[0] + r[2]) % w
            r[1] = (r[1] + r[3]) % h

            cols[r[0]] = cols[r[0]] + 1 if r[0] in cols else 1
            rows[r[1]] = rows[r[1]] + 1 if r[1] in rows else 1

        for r in d:
            if cols[r[0]] >= 31 and rows[r[1]] >= 31:
                no_tree = False
                break

    return s


def main():
    with open('in.txt') as file:
        d = [list(map(int, re.findall(r'-?\d+', line))) for line in file.readlines()]

        print('Part 1:', part_1(copy.deepcopy(d), 103, 101, 100))
        print('Part 2:', part_2(copy.deepcopy(d), 103, 101))


if __name__ == '__main__':
    main()