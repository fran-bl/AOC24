def part_1(data):
    diff = 0
    left, right = [], []

    for line in data:
        nums = line.split('   ')
        left.append(int(nums[0]))
        right.append(int(nums[1]))

    left.sort()
    right.sort()

    for i in range(len(left)):
        diff += abs(left[i] - right[i])

    return diff


def part_2(data):
    score = 0
    left, right = [], []

    for line in data:
        nums = line.split('   ')
        left.append(int(nums[0]))
        right.append(int(nums[1]))

    for el in left:
        score += el * right.count(el)

    return score


def main():
    with open('in.txt') as file:
        data = file.readlines()

        print('Part 1:', part_1(data))
        print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()