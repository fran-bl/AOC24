def find_cycles(G):
    cycles = set()

    for v in G:
        for n1 in G[v]:
            for n2 in G[v]:
                if n1 != n2 and n2 in G[n1]:
                    cycles.add(tuple(sorted((v, n1, n2))))

    return cycles


def bron_kerbosch(R, P, X, G, cliques):
    if not P and not X:
        cliques[frozenset(R)] = len(R)
        return
    
    for v in list(P):
        bron_kerbosch(R | {v}, P & G[v], X & G[v], G, cliques)
        P -= {v}
        X |= {v}


def part_1(G):
    cycles = find_cycles(G)
    cnt = 0

    for cycle in cycles:
        f = False

        for v in cycle:
            if v[0] == 't':
                f = True
                break

        if f:
            cnt += 1

    return cnt


def part_2(G):
    cliques = {}

    bron_kerbosch(set(), set(G.keys()), set(), G, cliques)

    return ','.join(sorted(list(max(cliques, key=cliques.get))))


def main():
    with open('in.txt') as file:
        data = file.readlines()

        G = {}

        for line in data:
            v1, v2 = line.rstrip().split('-')
            
            if v1 in G: G[v1].add(v2)
            else: G[v1] = set([v2])

            if v2 in G: G[v2].add(v1)
            else: G[v2] = set([v1])

        print('Part 1:', part_1(G))
        print('Part 2:', part_2(G))


if __name__ == '__main__':
    main()