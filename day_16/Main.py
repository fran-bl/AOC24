from queue import PriorityQueue


def adj(m, curr):
    d = curr[2]

    if (curr[0] + d[0], curr[1] + d[1]) in m:
        yield 1, (curr[0] + d[0], curr[1] + d[1], d)

    if (curr[0] - d[1], curr[1] + d[0]) in m:
        yield 1000, (*curr[:2], (-d[1], d[0]))
    
    if (curr[0] + d[1], curr[1] - d[0]) in m:
        yield 1000, (*curr[:2], (d[1], -d[0]))


def dijkstra(m, s, e):
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

    opt_dir = None
    min_d = float('inf')

    for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if (*e, direction) in d and min_d > d[(*e, direction)]:
            min_d = d[(*e, direction)]
            opt_dir = direction

    stack = [(*e, opt_dir)]
    visited = set(stack)

    while len(stack) > 0:
        curr = stack.pop(-1)
        for parent in paths[curr]:
            if parent not in visited:
                visited.add(parent)
                stack.append(parent)

    unique_cells = set(x[:2] for x in visited)

    return d[(*e, opt_dir)], len(unique_cells)


def solution(m, s, e):
    return dijkstra(m, s, e)


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

        res = solution(m, (*s, (0, 1)), e)
        print('Part 1:', res[0])
        print('Part 2:', res[1])


if __name__ == '__main__':
    main()