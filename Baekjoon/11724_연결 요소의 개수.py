from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = set()


def bfs(n):
    visited.add(n)
    temp = deque()
    temp.append(n)
    while True:
        a = temp.popleft()
        for g in graph[a]:
            if g not in visited:
                temp.append(g)
                visited.add(g)
        if len(temp) == 0:
            break


cnt = 0
for i in range(1, N+1):
    if i not in visited:
        bfs(i)
        cnt += 1

print(cnt)

