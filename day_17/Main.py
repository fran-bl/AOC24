import math


class Computer:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C


    def __dv(self, val):
        if val < 4:
            return math.trunc(self.A / 2 ** val)
        elif val == 4:
            return math.trunc(self.A / 2 ** self.A)
        elif val == 5:
            return math.trunc(self.A / 2 ** self.B)
        elif val == 6:
            return math.trunc(self.A / 2 ** self.C)
        
        return -1


    def adv(self, val):
        self.A = self.__dv(val)


    def bxl(self, val):
        self.B ^= val


    def bst(self, val):
        if val < 4:
            self.B = val % 8
        elif val == 4:
            self.B = self.A % 8
        elif val == 5:
            self.B = self.B % 8
        elif val == 6:
            self.B = self.C % 8

    
    def jnz(self, ptr, val):
        if self.A != 0:
            return val
        
        return ptr + 2


    def bxc(self, val):
        self.B ^= self.C

    
    def out(self, val):
        if val < 4:
            return val % 8
        elif val == 4:
            return self.A % 8
        elif val == 5:
            return self.B % 8
        elif val == 6:
            return self.C % 8

        return None

    
    def bdv(self, val):
        self.B = self.__dv(val)

    def cdv(self, val):
        self.C = self.__dv(val)

    
    def __str__(self):
        return f'A: {self.A}, B: {self.B}, C: {self.C}'


def part_1(regs, inpt):
    c = Computer(*regs)
    ptr = 0
    out = []
    
    while ptr < len(inpt) - 1:
        jmp_f = False
        match inpt[ptr]:
            case 0:
                c.adv(inpt[ptr + 1])
            case 1:
                c.bxl(inpt[ptr + 1])
            case 2:
                c.bst(inpt[ptr + 1])
            case 3:
                jmp_f = True
                ptr = c.jnz(ptr, inpt[ptr + 1])
            case 4:
                c.bxc(inpt[ptr + 1])
            case 5:
                out.append(c.out(inpt[ptr + 1]))
            case 6:
                c.bdv(inpt[ptr + 1])
            case 7:
                c.cdv(inpt[ptr + 1])

        if not jmp_f:
            ptr += 2

    return out


def part_2(inpt):
    valid = []
    todo = [(1, 0)]

    for l, a in todo:
        for a in range(a, a + 8):
            if part_1((a, 0, 0), inpt) == inpt[-l:]:
                if l == len(inpt):
                    valid.append(a)
                else:
                    todo.append((l + 1, a * 8))

    return min(valid)


def main():
    with open('in.txt') as file:
        data = file.read().split('\n\n')

        regs = tuple([int(l[12:]) for l in data[0].split('\n')])
        inpt = [int(n) for n in data[1][9:].split(',')]
        
        print('Part 1:', *part_1(regs, inpt))
        print('Part 2:', part_2(inpt))


if __name__ == '__main__':
    main()