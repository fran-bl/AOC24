import heapq
import numpy as np


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def near_path(path, cell):
    i, j = cell

    return (i + 1, j) in path or (i - 1, j) in path or (i, j + 1) in path or (i, j - 1) in path


def skip(wall, path):
    i, j = wall

    if (i - 1, j) in path and (i + 1, j) in path:
        return abs(path[(i - 1, j)] - path[(i + 1, j)]) - 2
    elif (i, j - 1) in path and (i, j + 1) in path:
        return abs(path[(i, j - 1)] - path[(i, j + 1)]) - 2

    return 0


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


def part_1(path, walls):
    count = 0 

    for wall in walls:
        if skip(wall, path) >= 100:
            count += 1

    return count


def part_2(path):
    count = 0

    for cell in path:
        for di in range(-20, 21):
            for dj in range(-20 + abs(di), 21 - abs(di)):
                hop = (cell[0] + di, cell[1] + dj)
                if hop in path:
                    if path[cell] - path[hop] - heuristic(cell, hop) >= 100:
                        count += 1

    return count


def main():
    with open('in.txt') as file:
        data = file.readlines()

        n = len(data)
        path, walls = {}, {}
        s = e = None

        for i in range(n):
            for j in range(n):
                if data[i][j] != '#':
                    path[(i, j)] = 0

                if data[i][j] == 'S':
                    s = (i, j)

                if data[i][j] == 'E':
                    e = (i, j)

        for i in range(n):
            for j in range(n):
                if data[i][j] == '#' and 0 < i < n - 1 and 0 < j < n - 1 and near_path(path, (i, j)):
                    walls[(i, j)] = True

        l, p = a_star(path, s, e)

        c = e
        while c != s:
            path[c] = l
            l -= 1
            c = p[c]

        print('Part 1:', part_1(path, walls))
        print('Part 2:', part_2(path))


if __name__ == '__main__':
    main()