wire1 = input()

wire1 = wire1.split(",")

wire2 = input()
wire2 = wire2.split(",")

visited = {}
overlap = []

pos = (0,0)
walks = 0
for w in wire1:
    direction = w[0]
    if direction == "R":
        for i in range(int(w[1:])):
            walks += 1
            pos = (pos[0], pos[1] + 1)
            visited[pos] = walks
    if direction == "L":
        for i in range(int(w[1:])):
            walks += 1
            pos = (pos[0], pos[1] - 1)
            visited[pos] = walks
    if direction == "U":
        for i in range(int(w[1:])):
            walks += 1
            pos = (pos[0]+1, pos[1])
            visited[pos] = walks
    if direction == "D":
        for i in range(int(w[1:])):
            walks += 1
            pos = (pos[0]-1, pos[1])
            visited[pos] = walks

def find_dist(p, w):
    overlap.append(w + visited[p])

pos = (0,0)
walks = 0
for w in wire2:
    direction = w[0]
    if direction == "R":
        for i in range(int(w[1:])):
            walks += 1
            pos = (pos[0], pos[1] + 1)
            if pos in visited:
                find_dist(pos, walks)
    if direction == "L":
        for i in range(int(w[1:])):
            walks += 1
            pos = (pos[0], pos[1] - 1)
            if pos in visited:
                find_dist(pos, walks)
    if direction == "U":
        for i in range(int(w[1:])):
            walks += 1
            pos = (pos[0]+1, pos[1])
            if pos in visited:
                find_dist(pos, walks)
    if direction == "D":
        for i in range(int(w[1:])):
            walks += 1
            pos = (pos[0]-1, pos[1])
            if pos in visited:
                find_dist(pos, walks)

overlap.sort()
print(f"overlap: {overlap}")
