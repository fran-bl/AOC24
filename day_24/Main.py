import copy


def part_1(wires, to_resolve):
    while len(to_resolve) != 0:
        for k, v in to_resolve.copy().items():
            if k[0] in wires and k[1] in wires:
                match v[1]:
                    case 'AND':
                        wires[v[0]] = wires[k[0]] & wires[k[1]]
                    case 'OR':
                        wires[v[0]] = wires[k[0]] | wires[k[1]]
                    case 'XOR':
                        wires[v[0]] = wires[k[0]] ^ wires[k[1]]

                to_resolve.pop(k, None)

    return int(''.join([str(wires[w]) for w in sorted([w for w in wires.keys() if w.startswith('z')], reverse=True)]), 2)


def part_2(wires, ops):
    wrong = set()
    highest = sorted([w for w in wires.keys() if w.startswith('z')])[-1]

    for k, v in ops.items():
        if v[0][0] == 'z' and v[1] != 'XOR' and v[0] != highest:
            wrong.add(v[0])

        if (
            v[1] == 'XOR' 
            and v[0][0] not in ['x', 'y', 'z']
            and k[0][0] not in ['x', 'y', 'z']
            and k[1][0] not in ['x', 'y', 'z']
        ):
            wrong.add(v[0])

        if v[1] == 'AND' and k[0] != 'x00' and k[1] != 'x00':
            for sk, sv, in ops.items():
                if v[0] in sk[:2] and sv[1] != 'OR':
                    wrong.add(v[0])
        
        if v[1] == 'XOR':
            for sk, sv, in ops.items():
                if v[0] in sk[:2] and sv[1] == 'OR':
                    wrong.add(v[0])

    return ','.join(sorted(wrong))


def main():
    with open('in.txt') as file:
        data = file.read().strip().split('\n\n')

        wires = {(args := line.rstrip().split(': '))[0]: int(args[1]) for line in data[0].split('\n')}
        to_resolve = {((args := line.rstrip().replace(' -> ', ' ').split())[0], args[2], args[3]): (args[3], args[1]) for line in data[1].split('\n')}

        print('Part 1:', part_1(wires, copy.deepcopy(to_resolve)))
        print('Part 2:', part_2(wires, to_resolve))


if __name__ == '__main__':
    main()