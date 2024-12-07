def chk_combinations(part, tval, prod, curr, end, res):
    if res > tval:
        return False
    elif res == tval and curr == end:
        return True
    
    if curr == end:
        return False
    
    return chk_combinations(part, tval, prod, curr + 1, end, res + prod[curr + 1]) + chk_combinations(part, tval, prod, curr + 1, end, res * prod[curr + 1]) + (chk_combinations(part, tval, prod, curr + 1, end, int(str(res) + str(prod[curr + 1]))) if part == 2 else 0)


def part_1(d):
    res = 0

    for tval in d.keys():
        prod = d[tval]

        if chk_combinations(1, tval, prod, 0, len(prod) - 1, prod[0]):
            res += tval

    return res


def part_2(d):
    res = 0

    for tval in d.keys():
        prod = d[tval]

        if chk_combinations(2, tval, prod, 0, len(prod) - 1, prod[0]):
            res += tval

    return res


def main():
    with open('in.txt') as file:
        data = file.readlines()
        d = {}

        for line in data:
            args = line.split(': ')
            tval = int(args[0])
            prod = list(map(int, args[1].split()))

            d[tval] = prod

        print('Part 1:', part_1(d))
        print('Part 2:', part_2(d))


if __name__ == '__main__':
    main()