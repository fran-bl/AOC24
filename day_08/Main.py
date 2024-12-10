def part_1(d, height, width):
    unique = set()

    for ant in d.keys():
        ants = d[ant]
        
        for i in range(len(ants) - 1):
            for j in range(i + 1, len(ants)):
                x1, y1, x2, y2 = ants[i][0], ants[i][1], ants[j][0], ants[j][1]

                diff_x, diff_y = x1 - x2, y1 - y2

                if 0 <= x1 + diff_x < height and 0 <= y1 + diff_y < width:
                    unique.add((x1 + diff_x, y1 + diff_y))

                if 0 <= x2 - diff_x < height and 0 <= y2 - diff_y < width:
                    unique.add((x2 - diff_x, y2 - diff_y))

    return len(unique)


def part_2(d, height, width):
    unique = set()

    for ant in d.keys():
        ants = d[ant]
        
        for i in range(len(ants) - 1):
            for j in range(i + 1, len(ants)):
                x1, y1, x2, y2 = ants[i][0], ants[i][1], ants[j][0], ants[j][1]

                diff_x, diff_y = x1 - x2, y1 - y2

                unique.add((x1, y1))
                unique.add((x2, y2))

                while 0 <= x1 + diff_x < height and 0 <= y1 + diff_y < width:
                    x1 += diff_x
                    y1 += diff_y
                    unique.add((x1, y1))

                while 0 <= x2 - diff_x < height and 0 <= y2 - diff_y < width:
                    x2 -= diff_x
                    y2 -= diff_y
                    unique.add((x2, y2))

    return len(unique)


def main():
    with open('in.txt') as file:
        data = [line.rstrip() for line in file]
        d = {}
        height, width = len(data), len(data[0])

        for i in range(height):
            for j in range(width):
                c = data[i][j]
                if c.isalnum():
                    if c in d:
                        d[c].append((i, j))
                    else:
                        d[c] = [(i, j)]

        print('Part 1:', part_1(d, height, width))
        print('Part 2:', part_2(d, height, width))


if __name__ == '__main__':
    main()