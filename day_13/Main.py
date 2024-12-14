import re
from fractions import Fraction


def solve_for(k, l, X, part):
    A = [[k[0], l[0]], [k[1], l[1]]]
	
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
	
    if d == 0:
        return (0, 0)
	
    d1 = X[0] * l[1] - l[0] * X[1]
    d2 = k[0] * X[1] - X[0] * k[1]

    x, y = Fraction(d1, d), Fraction(d2, d)

    if part == 1 and (x > 100 or y > 100):
        return (0, 0)

    if x < 0 or y < 0 or x.denominator != 1 or y.denominator != 1:
        return (0, 0)

    return (x, y)


def part_1(d):
    res = 0

    for s in d:
        ans = solve_for(s[0], s[1], s[2], 1)
        res += 3 * ans[0] + ans[1]

    return res


def part_2(d):
    res = 0

    for s in d:
        ns = [s[2][0] + 10000000000000, s[2][1] + 10000000000000]
        ans = solve_for(s[0], s[1], ns, 2)
        res += 3 * ans[0] + ans[1]

    return res


def main():
    with open('in.txt') as file:
        d = [[list(map(int, re.findall(r'[0-9]+', line))) for line in block.split('\n')] for block in file.read().strip().split('\n\n')]

        print('Part 1:', part_1(d))
        print('Part 2:', part_2(d))


if __name__ == '__main__':
    main()