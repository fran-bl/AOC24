def mnhtn(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def next_cell(path, cell, prev):
    i, j = cell
    
    for d in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if d in path and d != prev:
            return d

    return None


def construct_path(path, s, e):
    l = 0
    prev = None
    c = s

    while c != e:
        path[c] = l
        t = c
        c = next_cell(path, c, prev)
        prev = t
        l += 1

    path[c] = l


def skip(path, r, save):
    count = 0

    for cell in path:
        for di in range(-r, r + 1):
            for dj in range(-r + abs(di), r + 1 - abs(di)):
                hop = (cell[0] + di, cell[1] + dj)
                if hop in path:
                    if path[cell] - path[hop] - mnhtn(cell, hop) >= save:
                        count += 1

    return count


def part_1(path):
    return skip(path, 2, 100)


def part_2(path):
    return skip(path, 20, 100)


def main():
    with open('in.txt') as file:
        data = file.readlines()

        n = len(data)
        path = {}
        s = e = None

        for i in range(n):
            for j in range(n):
                if data[i][j] != '#':
                    path[(i, j)] = 0

                if data[i][j] == 'S':
                    s = (i, j)

                if data[i][j] == 'E':
                    e = (i, j)

        construct_path(path, s, e)

        print('Part 1:', part_1(path))
        print('Part 2:', part_2(path))


if __name__ == '__main__':
    main()