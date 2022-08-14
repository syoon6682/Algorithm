N, M = map(int, input().split())

visited = [N]

def bfs(m):
    cnt = 0
    point = 0
    while True:
        if m in visited:
            return cnt
        if visited[point] - 1 >= 0 and visited[point] - 1 not in visited:
            visited.append(visited[point] - 1)
        elif visited[point] + 1 <= 100000 and visited[point] + 1 not in visited:
            visited.append(visited[point] + 1)
        elif visited[point] * 2 <= 100000 and visited[point] * 2 not in visited:
            visited.append(visited[point] * 1)

        point += 1
        cnt += 1


print(bfs(M))