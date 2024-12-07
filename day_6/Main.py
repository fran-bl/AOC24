def get_start_pos(mat):
    height, width = len(mat), len(mat[0])

    for i in range(height):
        for j in range(width):
            if mat[i][j] == '^':
                return [i, j]
    
    return None


def get_obstacles(mat):
    obstacles = {}
    height, width = len(mat), len(mat[0])

    for i in range(height):
        for j in range(width):
            if mat[i][j] == '#':
                obstacles[(i, j)] = True

    return obstacles


def get_crosses(path):
    crosses = {}

    for key in path.keys():
        t = [k for k in path.keys() if k[0] == key[0] and k[1] == key[1]]
        if len(t) > 1:
            crosses[key[:2]] = [False, [(k[0] - int(k[2].real), k[1] - int(k[2].imag), k[2], k[3]) for k in t]]
    
    return crosses


def chk_good_path(obstacles, pos, height, width):
    exit_dir = pos[3]

    turns_set = set()

    while 0 <= pos[0] < height and 0 <= pos[1] < width: 
        if pos[0] + int(exit_dir.real) < 0 or pos[0] + int(exit_dir.real) >= height or pos[1] + int(exit_dir.imag) < 0 or pos[1] + int(exit_dir.imag) >= width:
            return True

        if (pos[0] + int(exit_dir.real), pos[1] + int(exit_dir.imag)) in obstacles:
            entry_dir = exit_dir
            exit_dir *= -1j

            if 0 <= pos[0] + int(exit_dir.real) < height and 0 <= pos[1] + int(exit_dir.imag) < width and (pos[0] + int(exit_dir.real), pos[1] + int(exit_dir.imag)) in obstacles:
                exit_dir *= -1j

            encoded_pos = f'{pos[0]:03}{pos[1]:03}{entry_dir}{exit_dir}'

            if encoded_pos in turns_set:

                return False
            else:
                turns_set.add(encoded_pos)

        pos[0] += int(exit_dir.real)
        pos[1] += int(exit_dir.imag)


def part_1(mat):
    path = {}
    unique = set()
    start = get_start_pos(mat)
    pos = get_start_pos(mat)
    obstacles = get_obstacles(mat)
    height, width = len(mat), len(mat[0])

    entry_dir = exit_dir = -1

    while 0 <= pos[0] < height and 0 <= pos[1] < width:
        unique.add((pos[0], pos[1]))
        
        if pos[0] + int(exit_dir.real) < 0 or pos[0] + int(exit_dir.real) >= height or pos[1] + int(exit_dir.imag) < 0 or pos[1] + int(exit_dir.imag) >= width:
            path[(pos[0], pos[1], entry_dir, exit_dir)] = None
            break

        if (pos[0] + int(exit_dir.real), pos[1] + int(exit_dir.imag)) in obstacles:
            entry_dir = exit_dir
            exit_dir *= -1j

            if 0 <= pos[0] + int(exit_dir.real) < height and 0 <= pos[1] + int(exit_dir.imag) < width and (pos[0] + int(exit_dir.real), pos[1] + int(exit_dir.imag)) in obstacles:
                exit_dir *= -1j

        path[(pos[0], pos[1], entry_dir, exit_dir)] = None
        entry_dir = exit_dir

        pos[0] += int(exit_dir.real)
        pos[1] += int(exit_dir.imag)

    return len(unique), path


def part_2(mat):
    count = 0

    start = get_start_pos(mat)
    obstacles = get_obstacles(mat)
    _, path = part_1(mat)
    crosses = get_crosses(path)
    height, width = len(mat), len(mat[0])

    moves = list(path.keys())

    for i in range(len(moves)):
        move = moves[i]

        if move[:2] in crosses and not crosses[move[:2]][0]:
            obstacles[move[:2]] = True

            crosses[move[:2]][0] = True
            count += not chk_good_path(obstacles, list(crosses[move[:2]][1][0]), height, width)

            obstacles.pop(move[:2], None)
        
        elif move[:2] not in crosses and move != (start[0], start[1], -1, -1):
            obstacles[move[:2]] = True
            
            count += not chk_good_path(obstacles, list(moves[i - 1]), height, width)

            obstacles.pop(move[:2], None)

    return count


def main():
    with open('in.txt') as file:
        data = file.readlines()
        mat = []

        for line in data:
            mat.append(list(line.rstrip()))

        print('Part 1:', part_1(mat)[0])
        print('Part 2:', part_2(mat))


if __name__ == '__main__':
    main()