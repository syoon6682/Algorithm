from collections import deque

M, N = map(int, input().split())

visited = deque()
tomato = list()
for n in range(N):
    temp = list(map(int, input().split()))
    tomato.append(temp)

minus = 0
one = 0
for n in range(N):
    for m in range(M):
        if tomato[n][m] == 1:
            visited.append([n, m])
            one += 1
        elif tomato[n][m] == -1:
            minus += 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
while True:
    if not visited:
        break
    else:
        end = len(visited)
        for _ in range(end):
            test = visited[0]
            for d in range(4):
                new_x = test[0] + dx[d]
                new_y = test[1] + dy[d]
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                    continue
                elif tomato[new_x][new_y] == 0:
                    visited.append([new_x, new_y])
                    tomato[new_x][new_y] = 1
                    one += 1
            visited.popleft()
        cnt += 1

if N*M-minus == one:
    print(cnt-1)
else:
    print(-1)


