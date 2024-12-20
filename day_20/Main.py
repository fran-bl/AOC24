import heapq
import numpy as np


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def skip(path, r):
    count = 0

    for cell in path:
        for di in range(-r, r + 1):
            for dj in range(-r + abs(di), r + 1 - abs(di)):
                hop = (cell[0] + di, cell[1] + dj)
                if hop in path:
                    if path[cell] - path[hop] - heuristic(cell, hop) >= 100:
                        count += 1

    return count


def a_star(cells, s, e):
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

    return len(fwd), path


def part_1(path, r):
    return skip(path, r)


def part_2(path, r):
    return skip(path, r)


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

        l, p = a_star(path, s, e)

        c = e
        while c != s:
            path[c] = l
            l -= 1
            c = p[c]

        print('Part 1:', part_1(path, 2))
        print('Part 2:', part_2(path, 20))


if __name__ == '__main__':
    main()