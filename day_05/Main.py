def chk_update_ret_error(rules, update):
    for i in range(1, len(update)):
        for j in range(i):
            if rules.get(update[i]) and update[j] in rules.get(update[i]):
                return i, j

    return None


def part_1(rules, updates):
    res = 0

    for update in updates:
        if not chk_update_ret_error(rules, update):
            res += update[len(update) // 2]

    return res


def part_2(rules, updates):
    res = 0

    for update in updates:
        incorrect = False

        while chk_update_ret_error(rules, update):
            incorrect = True
            error = chk_update_ret_error(rules, update)
            update[error[0]], update[error[1]] = update[error[1]], update[error[0]]
        
        if incorrect:
            res += update[len(update) // 2]

    return res


def main():
    with open('in.txt') as file:
        data = file.readlines()

        flag = False
        rules, updates = {}, []

        for line in data:
            if len(line.strip()) == 0:
                flag = True
                continue
            
            if flag:
                updates.append(list(map(int, line.split(','))))
            else:
                args = list(map(int, line.split('|')))
                if args[0] in rules:
                    rules[args[0]].append(args[1])
                else:
                    rules[args[0]] = [args[1]]

        print('Part 1:', part_1(rules, updates))
        print('Part 2:', part_2(rules, updates))


if __name__ == '__main__':
    main()