from inp10 import inp
import time
import math

# inp = """.#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##"""

# inp = """.#....#####...#..
# ##...##.#####..##
# ##...#...#.#####.
# ..#.....X...###..
# ..#.#.....#....##"""

inp = inp.split('\n')
inp = [[y for y in x] for x in inp]
print(inp)

# counts = []
# for i, a in enumerate(inp):
#     for j, b in enumerate(a):
#         if b != "#":
#             continue
#         count = set()
#         for x, s in enumerate(inp):
#             for y, c in enumerate(s):
#                 if c == "#" and not (x == i and y == j):
#                     length = (((x-i)**2 + (y-j)**2)**(1/2))
#                     vec = ((x-i)/length, (y-j)/length)
#                     flag = False
#                     for k, v in count:
#                         if (math.isclose(k, vec[0]) and math.isclose(v, vec[1])):
#                             flag = True
#                             break
#                     if not flag:
#                         count.add(vec)
#         print(count)
#         counts.append(((i, j), len(count)))
# print(counts)
#
# print(max(counts, key=lambda x: x[1]))

coord = (26, 29)
# coord = (11, 13)
# coord = (8, 3)
destroy = {}
angles = set()

for i, a in enumerate(inp):
    for j, b in enumerate(a):
        # destroy[j-coord[1], i-coord[0]](math.atan2(j-coord[1], i-coord[0]))
        print(b)
        if (j, i) == coord: continue
        if b == "#":
            print((j,i))
            ang = (math.atan2(i-coord[1], j-coord[0]))
            ang = ang + math.pi/2
            ang = ang if ang >= 0 else ang + 2 * math.pi
            if ang not in destroy:
                destroy[ang] = [(j, i)]
            else:
                destroy[ang].append((j, i))
            angles.add(ang)


angles = list(angles)
angles.sort()
ret = []
while destroy:
    i = 0
    while i < len(angles):
        if not destroy[angles[i]]:
            del destroy[angles[i]]
            del angles[i]
            continue
        destroy[angles[i]].sort(key=lambda x: abs(x[0] + x[1] - coord[0] - coord[1]), reverse=True)
        # if destroy[angles[i]][0] != coord[0] or destroy[angles[i][0]] != coord[1]:
        ret.append(destroy[angles[i]].pop())
        i += 1
    print(destroy)
    # time.sleep(1)


print(ret)
# print(inp)
# print(ret[299])
print(ret[200-1])
print(coord in ret)
