def flood_fill(pos, p, m, h, w, v):
    if m[pos[0]][pos[1]] != p:
        return [0, 1]

    if pos in v:
        return [0, 0]

    ret = [1, 0]
    v.add(pos)

    if pos[0] - 1 >= 0:
        res = flood_fill((pos[0] - 1, pos[1]), p, m, h, w, v)
        ret[0] += res[0]
        ret[1] += res[1]
    else:
        ret[1] += 1

    if pos[0] + 1 < h:
        res = flood_fill((pos[0] + 1, pos[1]), p, m, h, w, v)
        ret[0] += res[0]
        ret[1] += res[1]
    else:
        ret[1] += 1
    
    if pos[1] - 1 >= 0:
        res = flood_fill((pos[0], pos[1] - 1), p, m, h, w, v)
        ret[0] += res[0]
        ret[1] += res[1]
    else:
        ret[1] += 1
    
    if pos[1] + 1 < w:
        res = flood_fill((pos[0], pos[1] + 1), p, m, h, w, v)
        ret[0] += res[0]
        ret[1] += res[1]
    else:
        ret[1] += 1

    return ret


def flood_fill2(pos, p, m, h, w, v):
    if m[pos[0]][pos[1]] != p or pos in v:
        return [0, 0]

    v.add(pos)

    area = 1
    sides = 0

    if pos[0] - 1 < 0 or m[pos[0] - 1][pos[1]] != p:
        if pos[1] - 1 < 0 or m[pos[0]][pos[1] - 1] != p:
            sides += 1
    elif pos[1] - 1 >= 0 and m[pos[0]][pos[1] - 1] == p and m[pos[0] - 1][pos[1] - 1] != p:
        sides += 1
    
    if pos[0] - 1 < 0 or m[pos[0] - 1][pos[1]] != p:
        if pos[1] + 1 >= w or m[pos[0]][pos[1] + 1] != p:
            sides += 1
    elif pos[1] + 1 < w and m[pos[0]][pos[1] + 1] == p and m[pos[0] - 1][pos[1] + 1] != p:
        sides += 1
    
    if pos[0] + 1 >= h or m[pos[0] + 1][pos[1]] != p:
        if pos[1] + 1 >= w or m[pos[0]][pos[1] + 1] != p:
            sides += 1
    elif pos[1] + 1 < w and m[pos[0]][pos[1] + 1] == p and m[pos[0] + 1][pos[1] + 1] != p:
        sides += 1

    if pos[0] + 1 >= h or m[pos[0] + 1][pos[1]] != p:
        if pos[1] - 1 < 0 or m[pos[0]][pos[1] - 1] != p:
            sides += 1
    elif pos[1] - 1 >= 0 and m[pos[0]][pos[1] - 1] == p and m[pos[0] + 1][pos[1] - 1] != p:
        sides += 1

    if pos[0] - 1 >= 0:
        ret = flood_fill2((pos[0] - 1, pos[1]), p, m, h, w, v)
        area += ret[0]
        sides += ret[1]

    if pos[0] + 1 < h:
        ret = flood_fill2((pos[0] + 1, pos[1]), p, m, h, w, v)
        area += ret[0]
        sides += ret[1]
    
    if pos[1] - 1 >= 0:
        ret = flood_fill2((pos[0], pos[1] - 1), p, m, h, w, v)
        area += ret[0]
        sides += ret[1]
    
    if pos[1] + 1 < w:
        ret = flood_fill2((pos[0], pos[1] + 1), p, m, h, w, v)
        area += ret[0]
        sides += ret[1]

    return [area, sides]


def part_1(m, h, w):
    res = 0
    v = set()

    for i in range(h):
        for j in range(w):
            if (i, j) not in v:
                ans = flood_fill((i, j), m[i][j], m, h, w, v)
                res += ans[0] * ans[1]

    return res


def part_2(m, h, w):
    res = 0
    v = set()

    for i in range(h):
        for j in range(w):
            if (i, j) not in v:
                ans = flood_fill2((i, j), m[i][j], m, h, w, v)
                res += ans[0] * ans[1]

    return res


def main():
    with open('in.txt') as file:
        m = [list(line.rstrip()) for line in file]
        h, w = len(m), len(m[0])

        print('Part 1:', part_1(m, h, w))
        print('Part 2:', part_2(m, h, w))


if __name__ == '__main__':
    main()