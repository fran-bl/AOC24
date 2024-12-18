import heapq


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def part_1(cells, s, e):
    g = {c: float('inf') for c in cells.keys()}
    f = {c: float('inf') for c in cells.keys()}
    h = {c: heuristic(c, e) for c in cells.keys()}
    f[s], g[s] = h[s], 0

    op = []
    heapq.heappush(op, (f[s], s))
    path, visited = {}, set()
    found = False

    while len(op) != 0:
        curr = heapq.heappop(op)[1]

        if curr == e: found = True; break

        if curr in visited: continue

        visited.add(curr)

        for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            child = (curr[0] + d[0], curr[1] + d[1])

            if child in cells:
                tg = g[curr] + 1
                tf = tg + h[child]

                if tf < f[child]:
                    g[child] = tg
                    f[child] = tf
                    heapq.heappush(op, (tf, child))
                    path[child] = curr

    fwd = {}
    
    if found:
        c = e
        while c != s:
            fwd[path[c]] = c
            c = path[c]

    return len(fwd)


def part_2(walls, cells, s, e):
    for wall in walls:
        cells.pop(wall, None)

        if not part_1(cells, s, e):
            return f'{wall[1]},{wall[0]}'
    
    return None


def main():
    with open('in.txt') as file:
        s, e = (0, 0), (70,  70)
        first_n = 1024

        walls = [(int(b.split(',')[1]), int(b.split(',')[0])) for b in file.read().strip().split('\n')]
        cells = {}

        for i in range(e[0] + 1):
            for j in range(e[1] + 1):
                if (i, j) not in walls[:first_n]:
                    cells[(i, j)] = None

        
        print('Part 1:', part_1(cells, s, e))
        print('Part 2:', part_2(walls[first_n:], cells, s, e))


if __name__ == '__main__':
    main()