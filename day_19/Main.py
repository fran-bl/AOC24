def compute(dp, patterns, design):
    if design in dp:
        return dp[design]

    if len(design) == 0:
        return 1

    possible = 0
    for p in patterns:
        if design.startswith(p):
            possible += compute(dp, patterns, design[len(p):])

    dp[design] = possible

    return possible


def part_1(dp, patterns, designs):
    res = 0

    for design in designs:
        res += bool(compute(dp, patterns, design))

    return res


def part_2(dp, patterns, designs):
    res = 0

    for design in designs:
        res += compute(dp, patterns, design)

    return res


def main():
    with open('in.txt') as file:
        data = file.read().strip().split('\n\n')
        patterns = data[0].split(', ')
        designs = data[1].split('\n')

        dp = {}
        
        print('Part 1:', part_1(dp, patterns, designs))
        print('Part 1:', part_2(dp, patterns, designs))


if __name__ == '__main__':
    main()