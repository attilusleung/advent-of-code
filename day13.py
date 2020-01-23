import copy
import math
import time
from inp13 import inp as l_base

class intcomp:
    def __init__(self):
        self.l = copy.deepcopy(l_base)
        self.l.extend([0] * 100000)
        self.input = []
        self.out = []
        self.entry = 0
        self.end = False
        self.base = 0
        self.int_code()

    def get_position(self, mode, i):
        if mode == 0:
            return self.l[i]
        if mode == 1:
            return i
        if mode == 2:
            return self.l[i] + self.base

    def int_code(self):
        l = self.l
        def get_mode(opcode):
            C = (opcode % 1000)//100
            B = (opcode % 10000)//1000
            A = (opcode % 100000)//10000
            # print((C, B, A))
            return (C, B, A)

        i = self.entry

        def get_next(c, i, j):
            m = get_mode(c)
            # print(m)
            ret = [self.get_position(m[x], i+x+1) for x in range(0, j)]
            # print(ret)
            # return ret if j != 1 else ret[0]
            if j == 1: return ret[0]
            return ret

        while i < len(l):
            opcode = l[i]
            if opcode % 100 == 99:
                self.end = True
                break
            elif opcode % 100 == 1:
                a, b, c = get_next(opcode, i, 3)
                l[c] = l[a] + l[b]

                i += 4
            elif opcode % 100 == 2:
                a, b, c = get_next(opcode, i, 3)
                l[c] = l[a] * l[b]
                i += 4
            elif opcode % 100 == 3:
                if not self.input:
                    self.entry = i
                    return
                inp = self.input.pop(0)
                a = get_next(opcode, i, 1)
                l[a] = inp
                i += 2
            elif opcode % 100 == 4:
                a = get_next(opcode, i, 1)
                out = l[a]
                # print(out)
                self.out.append(out)
                i += 2
            elif opcode % 100 == 5:
                a, b = get_next(opcode, i, 2)
                if (l[a]) != 0:
                    i = l[b]
                else:
                    i += 3
            elif opcode % 100 == 6:
                a, b = get_next(opcode, i, 2)
                if (l[a]) == 0:
                    i = l[b]
                else:
                    i += 3
            elif opcode % 100 == 7:
                a, b, c = get_next(opcode, i, 3)
                if (l[a]) < (l[b]):
                    l[c] = 1
                else:
                    l[c] = 0
                i += 4
            elif opcode % 100 == 8:
                a, b, c = get_next(opcode, i, 3)
                if (l[a]) == (l[b]):
                    l[c] = 1
                else:
                    l[c] = 0
                i += 4
            elif opcode % 100 == 9:
                a = get_next(opcode, i, 1)
                self.base += l[a]
                i += 2
            else:
                print("diu")
                break

    def next(self, i):
        self.input.append(i)
        self.int_code()
        return self.out

c = intcomp()

screen = [[0] * 40 for _ in range(40)]
done = False


while not done:
    done = True
    while c.out:
        score = -1
        pos = (c.out.pop(0), c.out.pop(0))
        if pos == (-1, 0):
            score = c.out.pop(0)
        else:
            screen[pos[1]][pos[0]] = c.out.pop(0)
        for x in screen:
            for y in x:
                print(y, end = "")
            print()
        print("score", score)

    paddle = -1
    ball = -1



    for i, l in enumerate(screen):
        for j, p in enumerate(l):
            if p == 4:
                ball = j
            elif p == 3:
                paddle = j
            elif p == 2:
                done = False
    c.next(int(input()))

    # if paddle > ball:
    #     c.next(-1)
    # elif paddle < ball:
    #     c.next(1)
    # else:
    #     c.next(0)
