import sys

N, M = map(int, sys.stdin.readline().split())

graph = list()
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    new = list()
    for i in range(N):
        if i == 0:
            new.append(temp[i])
        else:
            new.append(new[i-1]+temp[i])
    graph.append(new)

for _ in range(M):
    point = list(map(int, sys.stdin.readline().split()))
    x_start = point[0]
    x_end = point[2]
    y_start = point[1]
    y_end = point[3]

    local_sum = 0
    for x in range(x_start-1, x_end):
        local_sum += graph[x][y_end-1]
        # print(local_sum)
        if y_start > 1:
            local_sum -= graph[x][y_start-2]
            # print(local_sum)

    print(local_sum)