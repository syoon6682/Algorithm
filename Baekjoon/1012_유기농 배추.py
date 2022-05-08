def bfs(x, y):
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [(x, y)]
    ground[y][x] = 0

    for v in visited:
        for d in delta:
            if v[0]-d[0] < 0 or v[0]-d[0] >= M or v[1]-d[1] < 0 or v[1]-d[1] >=N:
                continue
            new_x = v[0] - d[0]
            new_y = v[1] - d[1]
            if ground[new_y][new_x] == 1:
                ground[new_y][new_x] = 0
                visited.append((new_x, new_y))



T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    ground = [[0 for _ in range(M)] for _ in range(N)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1

    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1:
                cnt += 1
                bfs(j, i)

    print(cnt)


