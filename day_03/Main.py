import re


def part_1(data):
    res = 0

    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
    
    for match in matches:
        nums = list(map(int, match[4:-1].split(',')))
        res += nums[0] * nums[1]

    return res


def part_2(data):
    res = 0

    valid_blocks = re.findall(r"(do\(\).*?|^.*?)don't\(\)", data)

    for block in valid_blocks:
        res += part_1(block)

    return res


def main():
    with open('in.txt') as file:
        data = file.read().replace('\r', '').replace('\n', '')

        print('Part 1:', part_1(data))
        print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()