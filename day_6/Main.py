import copy
from tqdm import tqdm


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


def chk_good_path(obstacles, pos, height, width):
    exit_dir = -1

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
    path = set()
    start = get_start_pos(mat)
    pos = get_start_pos(mat)
    obstacles = get_obstacles(mat)
    height, width = len(mat), len(mat[0])

    exit_dir = -1

    while 0 <= pos[0] < height and 0 <= pos[1] < width:
        path.add((pos[0], pos[1]))
        
        if pos[0] + int(exit_dir.real) < 0 or pos[0] + int(exit_dir.real) >= height or pos[1] + int(exit_dir.imag) < 0 or pos[1] + int(exit_dir.imag) >= width:
            break

        if (pos[0] + int(exit_dir.real), pos[1] + int(exit_dir.imag)) in obstacles:
            exit_dir *= -1j

        pos[0] += int(exit_dir.real)
        pos[1] += int(exit_dir.imag)

    return len(path), list(path)


def part_2(mat):
    count = 0

    start = get_start_pos(mat)
    obstacles = get_obstacles(mat)
    _, path = part_1(mat)
    height, width = len(mat), len(mat[0])

    for i in tqdm(range(len(path)), desc='Computing...'):
        idx = path[i]
        
        if idx != (start[0], start[1]):
            obstacles[idx] = True
            
            if not chk_good_path(obstacles, start[:], height, width):
                count += 1

            obstacles.pop(idx, None)

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