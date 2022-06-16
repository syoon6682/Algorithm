from collections import deque
from copy import deepcopy
N = int(input())

color = list()
for _ in range(N):
    color.append(list(input()))

color_RGB = deepcopy(color)
color_RB = deepcopy(color)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def RGB():
    global N
    cnt = 0

    for n in range(N):
        for m in range(N):
            if color_RGB[n][m] != 0:
                std = color_RGB[n][m]
                visited = deque()
                visited.append([n, m])
                while True:
                    if len(visited) == 0:
                        break
                    else:
                        check = visited[0]
                        for d in range(4):
                            x = dx[d]
                            y = dy[d]
                            new_x = check[0] + x
                            new_y = check[1] + y
                            if new_x < 0 or new_y <0 or new_x >= N or new_y >= N:
                                continue
                            elif color_RGB[new_x][new_y] == std:
                                color_RGB[new_x][new_y] = 0
                                visited.append([new_x, new_y])
                        visited.popleft()
                cnt += 1

    return cnt


def RB():
    global N
    cnt = 0

    for n in range(N):
        for m in range(N):
            if color_RB[n][m] != 0:
                std = color_RB[n][m]
                if std == 'R' or std == 'G':
                    std = ['R', 'G']
                else:
                    std = ['B']
                visited = deque()
                visited.append([n, m])
                while True:
                    if len(visited) == 0:
                        break
                    else:
                        check = visited[0]
                        for d in range(4):
                            x = dx[d]
                            y = dy[d]
                            new_x = check[0] + x
                            new_y = check[1] + y
                            if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N:
                                continue
                            elif color_RB[new_x][new_y] in std:
                                color_RB[new_x][new_y] = 0
                                visited.append([new_x, new_y])
                        visited.popleft()
                cnt += 1

    return cnt


print(RGB(), RB())



