from inp12 import inp
from copy import deepcopy

inp = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]

past = set()

pos = inp
velocity = [[0, 0, 0] for i in range(len(pos))]

# count = 0
# while not ((tuple([tuple(x) for x in pos]), tuple([tuple(x) for x in velocity]))) in past:
#     past.add((tuple([tuple(x) for x in pos]), tuple([tuple(x) for x in velocity])))
#     for i, p in enumerate(pos):
#         for j, b in enumerate(pos):
#             if i == j: continue
#             for z in range(3):
#                 if p[z] > b[z]:
#                     velocity[i][z] -= 1
#                     # velocity[j][z] += 1
#                 elif p[z] < b[z]:
#                     velocity[i][z] += 1
#                     # velocity[j][z] -= 1
#         # print("v", velocity)
#     for i, e in enumerate(pos):
#         for z in range(3):
#             pos[i][z] += velocity[i][z]
#
# print(len(past))

past1 = set()
done1 = False
past2 = set()
done2 = False
past3 = set()
done3 = False
past4 = set()
done4 = False

past = [set() for i in range(3)]
done = [False] * 3

def make_all():
    return (tuple([tuple(x) for x in pos]), tuple([tuple(x) for x in velocity]))

def make_one(i):
    return (tuple(pos[i]), tuple(velocity[i]))

def make_dim(i):
    return (tuple([pos[x][i] for x in range(4)]), tuple([velocity[x][i] for x in range(4)]))

while not all(done):
    for i in range(3):
        past[i].add(make_dim(i))
    for i, p in enumerate(pos):
        for j, b in enumerate(pos):
            if i == j: continue
            for z in range(3):
                if p[z] > b[z]:
                    velocity[i][z] -= 1
                    # velocity[j][z] += 1
                elif p[z] < b[z]:
                    velocity[i][z] += 1
                    # velocity[j][z] -= 1
        # print("v", velocity)
    for i, e in enumerate(pos):
        for z in range(3):
            pos[i][z] += velocity[i][z]
    for i in range(3):
        # print(past)
        if make_dim(i) in past[i]:
            done[i] = len(past[i])

print(done)



#
# print(len(past))




# total = 0
# for i, p in enumerate(pos):
#     pot = 0
#     for q in p:
#         pot += abs(q)
#     kin = 0
#     for v in velocity[i]:
#         kin += abs(v)
#     total += (pot * kin)
#
# print(total)
