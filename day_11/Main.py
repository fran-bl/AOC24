def compute(num, d, blink):
    if blink == 0:
        return 1

    if (num, blink) in d:
        return d[(num, blink)]

    count = 0

    if num == 0:
        count += compute(1, d, blink - 1)
    elif len(str(num)) % 2 == 0:
        s_num = str(num)
        spl = len(s_num) // 2
        count += compute(int(s_num[:spl]), d, blink - 1)
        count += compute(int(s_num[spl:]), d, blink - 1)
    else:
        count += compute(num * 2024, d, blink - 1)

    d[(num, blink)] = count

    return count


def part_1(data):
    d = {}

    count = 0
    for num in data:
        count += compute(num, d, 25)

    return count


def part_2(data):
    d = {}

    count = 0
    for num in data:
        count += compute(num, d, 75)

    return count


def main():
    with open('in.txt') as file:
        data = list(map(int, file.read().split()))

        print('Part 1:', part_1(data))
        print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()