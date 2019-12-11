import copy
l_base = [3,8,1001,8,10,8,105,1,0,0,21,46,59,84,93,110,191,272,353,434,99999,3,9,101,2,9,9,102,3,9,9,1001,9,5,9,102,4,9,9,1001,9,4,9,4,9,99,3,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1001,9,4,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,3,9,4,9,99,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,99]
# l_base = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# l_base = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26, 27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# l_base = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
# -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
# 53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

class intcomp:
    def __init__(self, i):
        self.l = copy.deepcopy(l_base)
        self.input = [i]
        self.last_out = None
        self.entry = 0
        self.end = False
        self.int_code()

    def int_code(self):
        l = self.l
        def get_mode(opcode):
            C = (opcode % 1000)//100
            B = (opcode % 10000)//1000
            A = (opcode % 100000)//10000
            # print((C, B, A))
            return (C, B, A)

        i = self.entry

        while i < len(l):
            opcode = l[i]
            # print(opcode)
            if opcode % 100 == 99:
                self.end = True
                break
            elif opcode % 100 == 1:
                m = get_mode(opcode)
                if m[2] == 0:
                    l[l[i+3]] = (l[l[i+2]] if m[1] == 0 else l[i+2]) + (l[l[i+1]]if m[0] == 0 else l[i+1])
                else:
                    print("what")
                    l[i+3] = (l[l[i+2]] if m[1] == 0 else l[i+2]) + (l[l[i+1]]if m[0] == 0 else l[i+1])

                i += 4
            elif opcode % 100 == 2:
                m = get_mode(opcode)
                if m[2] == 0:
                    l[l[i+3]] = (l[l[i+2]] if m[1] == 0 else l[i+2]) * (l[l[i+1]]if m[0] == 0 else l[i+1])
                else:
                    print("what")
                    l[i+3] = (l[l[i+2]] if m[1] == 0 else l[i+2]) * (l[l[i+1]]if m[0] == 0 else l[i+1])
                i += 4
            elif opcode % 100 == 3:
                if not self.input:
                    self.entry = i
                    return
                print("get")
                inp = self.input.pop(0)
                m = get_mode(opcode)
                if m[0] == 0:
                    l[l[i+1]] = inp
                else:
                    print("what")
                    l[i+1] = inp
                i += 2
            elif opcode % 100 == 4:
                m = get_mode(opcode)
                out = l[l[i+1]] if m[0] == 0 else l[i+1]
                print(out)
                self.last_out = out
                i += 2
            elif opcode % 100 == 5:
                m = get_mode(opcode)
                if (l[l[i+1]] if m[0] == 0 else l[i+1]) != 0:
                    i = l[l[i+2]] if m[1] == 0 else l[i+2]
                else:
                    i += 3
            elif opcode % 100 == 6:
                m = get_mode(opcode)
                if (l[l[i+1]] if m[0] == 0 else l[i+1]) == 0:
                    i = l[l[i+2]] if m[1] == 0 else l[i+2]
                else:
                    i += 3
            elif opcode % 100 == 7:
                m = get_mode(opcode)
                if (l[l[i+1]] if m[0] == 0 else l[i+1]) < (l[l[i+2]] if m[1] == 0 else l[i+2]):
                    l[l[i+3]] = 1
                else:
                    l[l[i+3]] = 0
                i += 4
            elif opcode % 100 == 8:
                m = get_mode(opcode)
                if (l[l[i+1]] if m[0] == 0 else l[i+1]) == (l[l[i+2]] if m[1] == 0 else l[i+2]):
                    l[l[i+3]] = 1
                else:
                    l[l[i+3]] = 0
                i += 4
            else:
                print("diu")
                break

    def next(self, i):
        self.input.append(i)
        self.int_code()
        return self.last_out


m = -1
seq = []
for i in range(100000):
    flag = False
    j = [i//10000, (i//1000)% 10, (i//100) % 10, (i//10) % 10, i % 10]
    for c, e in enumerate(j):
        if e <= 4:
            flag = True
        for x, y in enumerate(j):
            if c != x and e == y:
                flag = True
    if not flag:
        seq.append(j)

# for s in seq:
#     c1 = intcomp(s[0])
#     c2 = intcomp(s[1])
#     c3 = intcomp(s[2])
#     c4 = intcomp(s[3])
#     c5 = intcomp(s[4])
#     i = c1.next(0)
#     i = c2.next(i)
#     i = c3.next(i)
#     i = c4.next(i)
#     i = c5.next(i)
#     print(i)
#     # m = max(i, m)

for s in seq:
    c1 = intcomp(s[0])
    c2 = intcomp(s[1])
    c3 = intcomp(s[2])
    c4 = intcomp(s[3])
    c5 = intcomp(s[4])
    i = c1.next(0)
    i = c2.next(i)
    i = c3.next(i)
    i = c4.next(i)
    i = c5.next(i)
    while not c5.end:
        i = c1.next(i)
        i = c2.next(i)
        i = c3.next(i)
        i = c4.next(i)
        i = c5.next(i)
    m = max(i, m)

print(m)

# print(l)
