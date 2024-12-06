import copy


def get_start_pos(mat):
    height, width = len(mat), len(mat[0])

    for i in range(height):
        for j in range(width):
            if mat[i][j] == '^':
                return [i, j]
    
    return None


def chk_good_path(mat):
    pos = get_start_pos(mat)
    height, width = len(mat), len(mat[0])

    directions = {
        0: [-1, 0],
        1: [0, 1],
        2: [1, 0],
        3: [0, -1]
    }
    curr_dir = 0

    turns_set = set()
    turns = 0

    while 0 <= pos[0] < height and 0 <= pos[1] < width: 
        if pos[0] + directions[curr_dir][0] < 0 or pos[0] + directions[curr_dir][0] >= height or pos[1] + directions[curr_dir][1] < 0 or pos[1] + directions[curr_dir][1] >= width:
            return True

        if mat[pos[0] + directions[curr_dir][0]][pos[1] + directions[curr_dir][1]] == '#':
            entry_dir = curr_dir
            curr_dir = (curr_dir + 1) % 4

            if 0 <= pos[0] + directions[curr_dir][0] < height and 0 <= pos[1] + directions[curr_dir][1] < width and mat[pos[0] + directions[curr_dir][0]][pos[1] + directions[curr_dir][1]] == '#':
                curr_dir = (curr_dir + 1) % 4

            turns_set.add(f'{pos[0]:03}{pos[1]:03}{entry_dir}{curr_dir}')
            turns += 1
            last_hit = (pos[0] + directions[curr_dir][0], pos[1] + directions[curr_dir][1])

            if len(turns_set) != turns:
                return False

        pos[0] += directions[curr_dir][0]
        pos[1] += directions[curr_dir][1]


def part_1(mat):
    count = 0

    path = copy.deepcopy(mat)
    start = get_start_pos(mat)
    pos = get_start_pos(mat)
    height, width = len(mat), len(mat[0])

    directions = {
        0: [-1, 0],
        1: [0, 1],
        2: [1, 0],
        3: [0, -1]
    }
    curr_dir = 0

    while 0 <= pos[0] < height and 0 <= pos[1] < width:
        path[pos[0]][pos[1]] = 'X'
        
        if pos[0] + directions[curr_dir][0] < 0 or pos[0] + directions[curr_dir][0] >= height or pos[1] + directions[curr_dir][1] < 0 or pos[1] + directions[curr_dir][1] >= width:
            break

        if mat[pos[0] + directions[curr_dir][0]][pos[1] + directions[curr_dir][1]] == '#':
            curr_dir = (curr_dir + 1) % 4

        pos[0] += directions[curr_dir][0]
        pos[1] += directions[curr_dir][1]

    for i in range(height):
        for j in range(width):
            if path[i][j] == 'X':
                count += 1

    return count, path


def part_2(mat):
    count = 0

    start = get_start_pos(mat)
    _, path = part_1(mat)
    height, width = len(mat), len(mat[0])

    for i in range(height):
        for j in range(width):
            if path[i][j] == 'X' and (i, j) != (start[0], start[1]):
                mat[i][j] = '#'
                
                if not chk_good_path(mat):
                    count += 1

                mat[i][j] = '.'

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