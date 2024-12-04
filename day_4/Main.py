def part_1(mat):
    count = 0

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'X':
                if i >= 3:
                    if mat[i - 1][j] == 'M' and mat[i - 2][j] == 'A' and mat[i - 3][j] == 'S':
                        count += 1

                    if j >= 3:
                        if mat[i - 1][j - 1] == 'M' and mat[i - 2][j - 2] == 'A' and mat[i - 3][j - 3] == 'S':
                            count += 1

                    if j < len(mat[i]) - 3:
                        if mat[i - 1][j + 1] == 'M' and mat[i - 2][j + 2] == 'A' and mat[i - 3][j + 3] == 'S':
                            count += 1

                if i < len(mat) - 3:
                    if mat[i + 1][j] == 'M' and mat[i + 2][j] == 'A' and mat[i + 3][j] == 'S':
                        count += 1

                    if j >= 3:
                        if mat[i + 1][j - 1] == 'M' and mat[i + 2][j - 2] == 'A' and mat[i + 3][j - 3] == 'S':
                            count += 1

                    if j < len(mat[i]) - 3:
                        if mat[i + 1][j + 1] == 'M' and mat[i + 2][j + 2] == 'A' and mat[i + 3][j + 3] == 'S':
                            count += 1

                if j >= 3:
                    if mat[i][j - 1] == 'M' and mat[i][j - 2] == 'A' and mat[i][j - 3] == 'S':
                        count += 1
                
                if j < len(mat[i]) - 3:
                    if mat[i][j + 1] == 'M' and mat[i][j + 2] == 'A' and mat[i][j + 3] == 'S':
                        count += 1

    return count


def part_2(mat):
    count = 0

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 'A':
                if i > 0 and i < len(mat) - 1 and j > 0 and j < len(mat[i]) - 1:
                    chars = [mat[i - 1][j - 1], mat[i - 1][j + 1], mat[i + 1][j - 1], mat[i + 1][j + 1]]
                    
                    if chars.count('M') == chars.count('S') == 2 and chars[0] != chars[3]:
                        count += 1

    return count


def main():
    with open('in.txt') as file:
        data = file.readlines()
        mat = []

        for line in data:
            mat.append(list(line.rstrip()))

        print('Part 1:', part_1(mat))
        print('Part 2:', part_2(mat))


if __name__ == '__main__':
    main()