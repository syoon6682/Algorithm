import sys

N, M, V = map(int, sys.stdin.readline().split())

graph = list([0] * (N+1) for _ in range(N+1))

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = 1
    graph[y][x] = 1


dfs_visited = [V]
bfs_visited = [V]


def dfs(v):
    global N
    if len(dfs_visited) == N:
        return

    else:
        for i in range(1, N+1):
            if (i not in dfs_visited) and (graph[v][i] == 1):
                dfs_visited.append(i)
                dfs(i)


def bfs():
    start = 0
    end = 1
    while True:

        for i in range(1, N+1):
            if (i not in bfs_visited) and (graph[bfs_visited[start]][i] == 1):
                bfs_visited.append(i)
                end += 1
        start += 1
        if start == end:
            return


dfs(V)
for d in dfs_visited:
    print(d, end=' ')

print()
bfs()
for b in bfs_visited:
    print(b, end=' ')