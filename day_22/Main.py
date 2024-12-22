from collections import Counter


def evolve(n):
    n = ((n * 64) ^ n) % 16777216
    n = ((n // 32) ^ n) % 16777216
    n = ((n * 2048) ^ n) % 16777216

    return n


def common_seq(seqs):
    dicts = []

    for l in seqs:
        d = {}

        for i in range(len(l) - 3):
            seq = tuple(l[i:i + 4])
            
            if seq not in d:
                d[seq] = i

        dicts.append(d)


    all_keys = Counter(k for d in dicts for k in d.keys())

    ranked = sorted(all_keys.items(), key=lambda item: item[1], reverse = True)

    return ranked, dicts


def part_1(nums):
    res = 0

    for num in nums:
        for _ in range(2000):
            num = evolve(num)

        res += num

    return res


def part_2(nums):
    seqs = []
    prices = []

    for num in nums:
        ch = []
        pr = []

        for _ in range(2000):
            t = evolve(num)
            ch.append(t % 10 - num % 10)
            num = t
            pr.append(num % 10)

        seqs.append(ch)
        prices.append(pr)

    ranked, dicts = common_seq(seqs)

    bananas = []

    for k, c in ranked:
        cnt = 0

        for i, d in enumerate(dicts):
            if k in d:
                cnt += prices[i][d[k] + 3]
            
        bananas.append(cnt)

    return max(bananas)


def main():
    with open('in.txt') as file:
        data = [int(num) for num in file.readlines()]
        
        print('Part 1:', part_1(data))
        print('Part 1:', part_2(data))


if __name__ == '__main__':
    main()