def check(levels):
    diffs = [levels[i] - levels[i + 1] for i in range(len(levels) - 1)]

    return 1 if all(el in [1, 2, 3] for el in diffs) or all(el in [-3, -2, -1] for el in diffs) else 0


def part_1(data):
    safe = 0

    for line in data:
        levels = [int(el) for el in line.split()]

        safe += check(levels)

    return safe


def part_2(data):
    safe = part_1(data)

    for line in data:
        levels = [int(el) for el in line.split()]

        if not check(levels):
            for i in range(len(levels)):
                new = levels.copy()
                new.pop(i)
                if check(new):
                    safe += 1
                    break

    return safe


def main():
    with open('in.txt') as file:
        data = file.readlines()

        print('Part 1:', part_1(data))
        print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()