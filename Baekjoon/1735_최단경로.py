import sys

V, E = map(int, sys.stdin.readline().split())
K = int(input())
inf = 3000000
graph = list([] for _ in range(V+1))

for _ in range(E):
    s, e, l = map(int, sys.stdin.readline().split())
    if e == K:
        continue
    graph[s].append([e, l])


length = [inf] * (V+1)
visited = [K]
checkout = [True] * (V+1)

start, end = 0, 1


def tester(node):

    for n in node:
        new = list()
        checkout[n] = False

        for i in graph[n]:
            target = i[0]
            info = i[1]

            if n == K:
                length[target] = info
                new.append(target)

            else:
                t = min(length[target], info + length[n])
                if length[target] > t:
                    length[target] = t
                    new.append(target)


temp = tester(visited)

while True:
    temp = tester(temp)
    if not temp:
        break


for p in range(1, V+1):
    if p == K:
        print(0)
    elif length[p] == inf:
        print('INF')
    else:
        print(length[p])
