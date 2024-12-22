def evolve(n, reps):
    nums, changes, prices = [], [], []

    for _ in range(reps):
        t = n
        n = ((n * 64) ^ n) % 16777216
        n = ((n // 32) ^ n) % 16777216
        n = ((n * 2048) ^ n) % 16777216
        nums.append(n)
        changes.append(n % 10 - t % 10)
        prices.append(n % 10)

    return nums, changes, prices


def part_1(nums):
    res = 0

    for num in nums:
        res += evolve(num, 2000)[0][-1]

    return res


def part_2(nums):
    d = {}

    for num in nums:
        seqs = set()
        
        _, ch, pr = evolve(num, 2000)

        for i in range(len(ch) - 3):
            seq = tuple(ch[i:i + 4])
            
            if seq not in seqs:
                d[seq] = d.get(seq, 0) + pr[i + 3]
                seqs.add(seq)

    return max(d.values())


def main():
    with open('in.txt') as file:
        nums = [int(num) for num in file.readlines()]
        
        print('Part 1:', part_1(nums))
        print('Part 1:', part_2(nums))


if __name__ == '__main__':
    main()