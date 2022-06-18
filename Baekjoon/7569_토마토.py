from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().split())

minus = 0
one = 0
visited = deque()
tomato = list()
for h in range(H):
    temp = list()
    for _ in range(N):
        temp.append(list(map(int, stdin.readline().split())))
    tomato.append(temp)

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                visited.append([h, n, m])
                one += 1
            elif tomato[h][n][m] == -1:
                minus += 1

cnt = 0
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

while True:
    if not visited:
        break
    else:
        end = len(visited)
        for _ in range(end):
            test = visited[0]
            for d in range(6):
                new_x = test[0] + dx[d]
                new_y = test[1] + dy[d]
                new_z = test[2] + dz[d]
                if new_x < 0 or new_x >= H or new_y < 0 or new_y >= N or new_z < 0 or new_z >= M:
                    continue
                elif tomato[new_x][new_y][new_z] == 0:
                    tomato[new_x][new_y][new_z] = 1
                    one += 1
                    visited.append([new_x, new_y, new_z])
            visited.popleft()
        cnt += 1

if N*M*H - minus == one:
    print(cnt -1)
else:
    print(-1)
