import re


def part_1(data):
    res = 0

    matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
    
    for match in matches:
        nums = re.findall(r'\d+', match)
        res += int(nums[0]) * int(nums[1])

    return res


def part_2(data):
    res = 0

    matches = re.finditer(r'mul\(\d{1,3},\d{1,3}\)', data)
    good_intervals = [[i.start(), i.end()] for i in re.finditer(r"(do\(\).*?|^.*?)don't\(\)", data)]

    for match in matches:
        for start, end in good_intervals:
            if start <= match.start() <= end:
                nums = re.findall(r'\d+', match.group())
                res += int(nums[0]) * int(nums[1])
                break

    return res


def main():
    with open('in.txt') as file:
        data = file.read().replace('\r', '').replace('\n', '')

        print('Part 1:', part_1(data))
        print('Part 2:', part_2(data))


if __name__ == '__main__':
    main()