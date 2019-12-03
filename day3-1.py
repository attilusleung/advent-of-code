wire1 = input()

wire1 = wire1.split(",")

wire2 = input()
wire2 = wire2.split(",")

visited = set()
overlap = []

pos = (0,0)
for w in wire1:
    direction = w[0]
    if direction == "R":
        for i in range(int(w[1:])):
            pos = (pos[0], pos[1] + 1)
            visited.add(pos)
    if direction == "L":
        for i in range(int(w[1:])):
            pos = (pos[0], pos[1] - 1)
            visited.add(pos)
    if direction == "U":
        for i in range(int(w[1:])):
            pos = (pos[0]+1, pos[1])
            visited.add(pos)
    if direction == "D":
        for i in range(int(w[1:])):
            pos = (pos[0]-1, pos[1])
            visited.add(pos)

def find_dist(p):
    dist = abs(p[0]) + abs(p[1])
    overlap.append(dist)

pos = (0,0)
for w in wire2:
    direction = w[0]
    if direction == "R":
        for i in range(int(w[1:])):
            pos = (pos[0], pos[1] + 1)
            if pos in visited:
                find_dist(pos)
    if direction == "L":
        for i in range(int(w[1:])):
            pos = (pos[0], pos[1] - 1)
            if pos in visited:
                find_dist(pos)
    if direction == "U":
        for i in range(int(w[1:])):
            pos = (pos[0]+1, pos[1])
            if pos in visited:
                find_dist(pos)
    if direction == "D":
        for i in range(int(w[1:])):
            pos = (pos[0]-1, pos[1])
            if pos in visited:
                find_dist(pos)

overlap.sort()
print(f"overlap: {overlap}")
