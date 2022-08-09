import sys

N, M, B = map(int, sys.stdin.readline().split())
global_min, global_max = 256, 0
global_sum = 0
ground = list()

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    if min(temp) < global_min:
        global_min = min(temp)
    elif max(temp) > global_max:
        global_max = max(temp)
    global_sum += sum(temp)
    ground.append(temp)

global_sum += B
avg_h = global_sum // (N * M)

global_sol = [1280000000, 0]

if avg_h > global_max:
    std = global_max
else:
    std = avg_h


while True:
    block = B
    time = 0
    for n in range(N):
        for m in range(M):
            if ground[n][m] - std > 0:
                time += (ground[n][m] - std) * 2
                block += (ground[n][m] - std)
            elif ground[n][m] - std < 0:
                time += (std - ground[n][m])
                block -= (std - ground[n][m])

    if time < global_sol[0]:
        global_sol = [time, std]
    else:
        break

    if std == global_min:
        break

    std -= 1

print(global_sol[0], global_sol[1])

