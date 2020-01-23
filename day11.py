import copy
import math
import time
from inp11 import l_base

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
                print(out)
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
board = [[0 for _ in range(100)] for _ in range(100)]
pos = (50, 50)
board[pos[1]][pos[0]] = 1
direction = math.pi/2
painted = set()
moves = 0

while not c.end:
    print(pos not in painted)
    print(f"adding {pos} to painted")
    painted.add(pos)
    moves += 1
    color = int(board[pos[1]][pos[0]])
    print("color", color)
    c.next(color)
    print(c.out)
    newc = c.out.pop(0)
    print("newc", newc)
    board[pos[1]][pos[0]] = newc
    turn = c.out.pop(0)

    if turn == 0:
        direction += math.pi/2
    elif turn == 1:
        direction -= math.pi/2
    print("turn", direction)

    assert abs(int(round(math.cos(direction)))) + abs(int(round(math.sin(direction)))) == 1

    pos = (pos[0] + int(round(math.cos(direction))), pos[1] + int(round(-math.sin(direction))))
    print(pos)
    print(direction)

print(painted)
print(moves)
print(len(painted))
print(pos)
print(pos in painted)
print((50, 50) in painted)

for a in board:
    for b in a:
        print(b, end="")
    print()
