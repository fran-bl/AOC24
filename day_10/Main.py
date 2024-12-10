def walk_path(data, pos, unique, height, width, curr):
    if curr == 9:
        unique.append(pos)
        return
    
    if pos[0] - 1 >= 0 and data[pos[0] - 1][pos[1]] == curr + 1:
        walk_path(data, (pos[0] - 1, pos[1]), unique, height, width, curr + 1)

    if pos[0] + 1 < height and data[pos[0] + 1][pos[1]] == curr + 1:
        walk_path(data, (pos[0] + 1, pos[1]), unique, height, width, curr + 1)

    if pos[1] - 1 >= 0 and data[pos[0]][pos[1] - 1] == curr + 1:
        walk_path(data, (pos[0], pos[1] - 1), unique, height, width, curr + 1)

    if pos[1] + 1 < width and data[pos[0]][pos[1] + 1] == curr + 1:
        walk_path(data, (pos[0], pos[1] + 1), unique, height, width, curr + 1)       


def part_1(data, th, height, width):
    score = 0
    unique = []

    for head in th:
        walk_path(data, head, unique, height, width, 0)
        score += len(set(unique))
        unique.clear()

    return score


def part_2(data, th, height, width):
    paths = []

    for head in th:
        walk_path(data, head, paths, height, width, 0)

    return len(paths)


def main():
    with open('in.txt') as file:
        data = [list(map(int, list(line.rstrip()))) for line in file]
        th = []
        height, width = len(data), len(data[0])

        for i in range(height):
            for j in range(width):
                if data[i][j] == 0:
                    th.append((i, j))

        print('Part 1:', part_1(data, th, height, width))
        print('Part 2:', part_2(data, th, height, width))


if __name__ == '__main__':
    main()