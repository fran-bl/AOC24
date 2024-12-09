import copy


def part_1(data):
    res = 0

    i, j = 0, len(data) - 1
    idx_i, idx_j = 0, len(data) // 2
    disk = []
    flag = False

    while i < j:
        disk.extend([idx_i] * data[i])

        if data[i + 1] < data[j]:
            disk.extend([idx_j] * data[i + 1])
            data[j] -= data[i + 1]
        else:
            while data[i + 1] > 0 and i < j:
                if data[i + 1] - data[j] < 0:
                    disk.extend([idx_j] * data[i + 1])
                    t = data[j]
                    data[j] -= data[i + 1]
                    data[i + 1] -= t
                else:
                    disk.extend([idx_j] * data[j])
                    data[i + 1] -= data[j]
                    j -= 2
                    idx_j -= 1

                    if i >= j:
                        flag = True 

        i += 2
        idx_i += 1

    if not flag:
        disk.extend([idx_j] * data[j])

    for i in range(len(disk)):
        res += disk[i] * i

    return res


def part_2(data):
    res = 0

    i, j = 0, len(data) - 1
    idx_i, idx_j = 0, len(data) // 2
    disk = []
    moved = set()

    while i < len(data) - 1:
        if i in moved:
            disk.extend([0] * data[i])
        else:
            disk.extend([idx_i] * data[i])

        gap = data[i + 1]

        t_j = j
        t_idx_j = idx_j

        while gap > 0 and i < t_j:
            if data[t_j] <= gap and t_j not in moved:
                disk.extend([t_idx_j] * data[t_j])
                gap -= data[t_j]
                moved.add(t_j)
            
            t_j -= 2            
            t_idx_j -= 1
            
        disk.extend([0] * gap)
        idx_i += 1
        i += 2

    for i in range(len(disk)):
        res += disk[i] * i

    return res
            

def main():
    with open('in.txt') as file:
        data = list(map(int, list(file.read().rstrip())))

        print('Part 1:', part_1(copy.copy(data)))
        print('Part 2:', part_2(copy.copy(data)))


if __name__ == '__main__':
    main()