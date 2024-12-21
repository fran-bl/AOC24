from collections import Counter


def steps(d, s, i):
    px, py = d['A']
    sx, sy = d[' ']
    ret = Counter()

    for c in s:
        nx, ny = d[c]
        f = nx == sx and py == sy or ny == sy and px == sx
        ret[(nx - px, ny - py, f)] += i
        px, py = nx, ny

    return ret


def compute(keypad, dirpad, data, n):
    res = 0

    for code in data:
        cnt = steps(keypad, code, 1)

        for _ in range(n + 1):
            cnt = sum([steps(dirpad, ('<' * -x + 'v' * y + '^' * -y + '>' * x)[:: -1 if f else 1] + 'A', cnt[(x, y, f)]) for x, y, f in cnt], Counter())

        res += cnt.total() * int(code[:3])

    return res


def part_1(keypad, dirpad, data):
    return compute(keypad, dirpad, data, 2)
    

def part_2(keypad, dirpad, data):
    return compute(keypad, dirpad, data, 25)


def main():
    with open('in.txt') as file:
        data = file.read().strip().split('\n')

        keypad = {c: (i % 3, i // 3) for i, c in enumerate("789456123 0A")}
        dirpad = {c: (i % 3, i // 3) for i, c in enumerate(" ^A<v>")}
        
        print('Part 1:', part_1(keypad, dirpad, data))
        print('Part 1:', part_2(keypad, dirpad, data))

if __name__ == '__main__':
    main()