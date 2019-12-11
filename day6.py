from input6 import inp

lines = [i.split(")") for i in inp.split("\n")]

nodes = set()
for i in lines:
    print(i)
    nodes.add(i[0])
    nodes.add(i[1])

edges = {}

for i, j in lines:
    if j in edges:
        edges[j].append(i)
    else:
        edges[j] = [i]
    if i in edges:
        edges[i].append(j)
    else:
        edges[i] = [j]

visited = {}
queue = []
def search(m):
    if m == "SAN":
        return (True, 0)
    if m in visited:
        return (False, -1)
    visited[m] = True
    for n in edges[m]:
        ret = search(n)
        if ret[0]:
            return (True, ret[1] + 1)
    return (False, -1)

def search(m, n):
    if m == "SAN":
        return (True, n+1)
    if m in visited:
        return (False, -1)
    visited[m] == True
    for n in edges[m]:
        queue.append((n, n+1))


print(search("YOU"))
