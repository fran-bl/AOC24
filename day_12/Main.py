def flood_fill(start, plot, data, height, width, visited):
    if data[start[0]][start[1]] != plot:
        return [0, 1]

    if start in visited:
        return [0, 0]

    ret = [1, 0]
    visited.add(start)

    if start[0] - 1 >= 0:
        res = flood_fill((start[0] - 1, start[1]), plot, data, height, width, visited)

        ret[0] += res[0]
        ret[1] += res[1]
    else:
        ret[1] += 1

    if start[0] + 1 < height:
        res = flood_fill((start[0] + 1, start[1]), plot, data, height, width, visited)

        ret[0] += res[0]
        ret[1] += res[1]
    else:
        ret[1] += 1
    
    if start[1] - 1 >= 0:
        res = flood_fill((start[0], start[1] - 1), plot, data, height, width, visited)

        ret[0] += res[0]
        ret[1] += res[1]
    else:
        ret[1] += 1
    
    if start[1] + 1 < width:
        res = flood_fill((start[0], start[1] + 1), plot, data, height, width, visited)

        ret[0] += res[0]
        ret[1] += res[1]
    else:
        ret[1] += 1

    return ret


sides = 0
def flood_fill2(start, plot, data, height, width, visited):
    if data[start[0]][start[1]] != plot or start in visited:
        return 0

    global sides

    ret = 1
    s = [0, 0, 0, 0]
    visited.add(start)

    if start[0] - 1 >= 0:
        if data[start[0] - 1][start[1]] != plot:
            s[0] = 1

        if start[1] - 1 >= 0:
            if data[start[0] - 1][start[1] - 1] != plot and data[start[0] - 1][start[1]] == data[start[0]][start[1] - 1] == plot:
                sides += 1

        ret += flood_fill2((start[0] - 1, start[1]), plot, data, height, width, visited)
    else:
        s[0] = 1

    if start[0] + 1 < height:
        if data[start[0] + 1][start[1]] != plot:
            s[2] = 1

        if start[1] + 1 < width:
            if data[start[0] + 1][start[1] + 1] != plot and data[start[0] + 1][start[1]] == data[start[0]][start[1] + 1] == plot:
                sides += 1

        ret += flood_fill2((start[0] + 1, start[1]), plot, data, height, width, visited)
    else:
        s[2] = 1
    
    if start[1] - 1 >= 0:
        if data[start[0]][start[1] - 1] != plot:
            s[3] = 1

        if start[0] + 1 < height:
            if data[start[0] + 1][start[1] - 1] != plot and data[start[0] + 1][start[1]] == data[start[0]][start[1] - 1] == plot:
                sides += 1

        ret += flood_fill2((start[0], start[1] - 1), plot, data, height, width, visited)
    else:
        s[3] = 1
    
    if start[1] + 1 < width:
        if data[start[0]][start[1] + 1] != plot:
            s[1] = 1

        if start[0] - 1 >= 0:
            if data[start[0] - 1][start[1] + 1] != plot and data[start[0] - 1][start[1]] == data[start[0]][start[1] + 1] == plot:
                sides += 1

        ret += flood_fill2((start[0], start[1] + 1), plot, data, height, width, visited)
    else:
        s[1] = 1

    for i in range(4):
        if s[i] == s[(i + 1) % 4] == 1:
            sides += 1

    return ret


def part_1(data, height, width):
    res = 0
    visited = set()

    for i in range(height):
        for j in range(width):
            if (i, j) not in visited:
                l = flood_fill((i, j), data[i][j], data, height, width, visited)
                res += l[0] * l[1]

    return res


def part_2(data, height, width):
    res = 0
    visited = set()

    global sides

    for i in range(height):
        for j in range(width):
            if (i, j) not in visited:
                sides = 0
                res += flood_fill2((i, j), data[i][j], data, height, width, visited) * sides

    return res


def main():
    with open('in.txt') as file:
        data = [list(line.rstrip()) for line in file]
        height, width = len(data), len(data[0])

        print('Part 1:', part_1(data, height, width))
        print('Part 2:', part_2(data, height, width))


if __name__ == '__main__':
    main()