import copy


def convert(m_old):
    pos = None
    m = {}

    i, j = 0, 0
    for k, v in m_old.items():
        if k[0] != i:
            i = k[0]
            j = 0

        match v:
            case '#':
                m[(i, j)] = '#'
                m[(i, j + 1)] = '#'
            case 'O':
                m[(i, j)] = '['
                m[(i, j + 1)] = ']'
            case '.':
                m[(i, j)] = '.'
                m[(i, j + 1)] = '.'
            case '@':
                pos = [i, j]
                m[(i, j)] = '@'
                m[(i, j + 1)] = '.'
        
        j += 2

    return m, pos


def cc(m, pos, dy, d):
    if pos in d:
        return

    if m[pos] == '[' or m[pos] == ']':
        d[pos] = m[pos]
    else:
        return

    if m[pos] == ']':
        cc(m, (pos[0], pos[1] - 1), dy, d)
    else:
        cc(m, (pos[0], pos[1] + 1), dy, d)

    cc(m, (pos[0] + dy, pos[1]), dy, d)


def move(m, pos, dy, dx):
    if m[(pos[0] + dy, pos[1] + dx)] == '.':
        m[(pos[0], pos[1])] = '.'
        pos[0] += dy
        pos[1] += dx
        m[(pos[0], pos[1])] = '@'

    elif m[(pos[0] + dy, pos[1] + dx)] == 'O':
        tdx, tdy = 2, 2

        while m[(pos[0] + tdy * dy, pos[1] + tdx * dx)] == 'O':
            tdx += 1
            tdy += 1

        if m[(pos[0] + tdy * dy, pos[1] + tdx * dx)] == '.':
            m[(pos[0] + tdy * dy, pos[1] + tdx * dx)] = 'O'
            m[(pos[0], pos[1])] = '.'
            pos[0] += dy
            pos[1] += dx
            m[(pos[0], pos[1])] = '@'


def move_2(m, pos, dy, dx):
    if dy == 0:
        if m[(pos[0], pos[1] + dx)] == '.':
            m[(pos[0], pos[1])] = '.'
            pos[1] += dx
            m[(pos[0], pos[1])] = '@'

        elif m[(pos[0], pos[1] + dx)] != '#':
            tdx = 3

            while m[(pos[0], pos[1] + tdx * dx)] != '#' and m[(pos[0], pos[1] + tdx * dx)] != '.':
                tdx += 1

            if m[(pos[0], pos[1] + tdx * dx)] == '.':
                for i in range(tdx):
                    m[(pos[0], pos[1] + tdx * dx + i * -dx)] = m[(pos[0], pos[1] + tdx * dx + (i + 1) * -dx)]

                m[(pos[0], pos[1])] = '.'
                pos[1] += dx

    else:
        if m[(pos[0] + dy, pos[1])] == '.':
            m[(pos[0], pos[1])] = '.'
            pos[0] += dy
            m[(pos[0], pos[1])] = '@'

        elif m[(pos[0] + dy, pos[1])] != '#':
            boxes = {}
            cc(m, (pos[0] + dy, pos[1]), dy, boxes)

            if all([m[(b[0] + dy, b[1])] != '#' for b in boxes.keys()]):
                for b in boxes.keys():
                    m[(b[0] + dy, b[1])] = boxes[b]
                    m[b] = boxes[(b[0] - dy, b[1])] if (b[0] - dy, b[1]) in boxes else '.'
                
                m[(pos[0], pos[1])] = '.'
                pos[0] += dy
                m[(pos[0], pos[1])] = '@'



def part_1(m, p, pos):
    res = 0

    for mov in p:
        match mov:
            case '^':
                move(m, pos, -1, 0)
            case '>':
                move(m, pos, 0, +1)
            case 'v':
                move(m, pos, +1, 0)
            case '<':
                move(m, pos, 0, -1)

    for k, v in m.items():
        if v == 'O':
            res += k[0] * 100 + k[1]

    return res


def part_2(m_old, p):
    res = 0
    m, pos = convert(m_old)

    for mov in p:
        match mov:
            case '^':
                move_2(m, pos, -1, 0)
            case '>':
                move_2(m, pos, 0, +1)
            case 'v':
                move_2(m, pos, +1, 0)
            case '<':
                move_2(m, pos, 0, -1)

    for k, v in m.items():
        if v == '[':
            res += k[0] * 100 + k[1]

    return res
    

def main():
    with open('in.txt') as file:
        data = file.read().split('\n\n')

        s = None
        m = {}
        p = data[1].replace('\n', '')

        for i, line in enumerate(data[0].split('\n')):
            for j, c in enumerate(list(line.rstrip())):
                if c == '@':
                    s = [i, j]
                
                m[(i, j)] = c

        print('Part 1:', part_1(copy.deepcopy(m), p, s))
        print('Part 2:', part_2(copy.deepcopy(m), p))


if __name__ == '__main__':
    main()