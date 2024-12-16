from queue import PriorityQueue


def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def adj(m, curr):
    d = curr[2]

    if (curr[0] + d[0], curr[1] + d[1]) in m:
        yield 1, (curr[0] + d[0], curr[1] + d[1], d)

    yield 1000, (*curr[:2], (-d[1], d[0]))
    yield 1000, (*curr[:2], (d[1], -d[0]))


def part_1(m, s, e):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    g = {cell: float('inf') for cell in m.keys()}
    g[s] = 0
    f = {cell: float('inf') for cell in m.keys()}
    f[s] = h(s, e)

    op = PriorityQueue()
    op.put((f[s], s, (0, 1)))

    while not op.empty():
        _, curr, p_dir = op.get()

        for d in dirs:
            if d == (-p_dir[0], -p_dir[1]):
                continue

            child = (curr[0] + d[0], curr[1] + d[1])

            if child in m:
                tg = g[curr] + 1 + (1000 if p_dir != d else 0)
                tf = tg + h(child, e)

                if tg < g[child]:
                    g[child] = tg
                    f[child] = tf
                    op.put((tf, child, d))

    return g[e]


def part_2(m, s, e):
    s = (*s, (0, 1))

    d = {}
    d[s] = 0

    paths = {s: []}

    op = PriorityQueue()
    op.put((d[s], s))

    while not op.empty():
        dist, curr = op.get()

        for d_ad, ad in adj(m, curr):
            if ad not in d or d_ad + dist < d[ad]:
                d[ad] = dist + d_ad
                op.put((d[ad], ad))
                paths[ad] = [curr]
            elif d_ad + dist == d[ad]:
                paths[ad].append(curr)

    minm = part_1(m, s, e)
    direction = None

    for i in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if d[(*e, i)] == minm:
            direction = i
            break

    stack = [(*e, direction)]
    visited = set(stack)

    while len(stack) > 0:
        curr = stack.pop(-1)
        for parent in paths[curr]:
            if parent not in visited:
                visited.add(parent)
                stack.append(parent)

    unique_cells = set(x[:2] for x in visited)

    return len(unique_cells)


def main():
    with open('in.txt') as file:
        data = file.read()

        s = e = None
        m = {}

        for i, line in enumerate(data.split('\n')):
            for j, c in enumerate(list(line.rstrip())):
                if c == 'S':
                    s = (i, j)

                if c == 'E':
                    e = (i, j)

                if c != '#':
                    m[(i, j)] = c

        print('Part 1:', part_1(m, s, e))
        print('Part 2:', part_2(m, s, e))


if __name__ == '__main__':
    main()