from collections import deque

com = int(input())
N = int(input())

network = list([0]*(com+1) for _ in range(com+1))

for _ in range(N):
    a, b = map(int, input().split())
    network[a][b] = 1
    network[b][a] = 1

d = deque([1])
visited = [1]


def bfs():
    global com
    while True:
        if len(d) == 0:
            print(len(visited)-1)
            return
        else:
            point = d[0]
            for i in range(com+1):
                if network[point][i] == 1 and i not in visited:
                    visited.append(i)
                    d.append(i)
            d.popleft()


bfs()