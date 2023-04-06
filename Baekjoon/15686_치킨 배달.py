import itertools
import sys

N, M = map(int, sys.stdin.readline().split())

home = list()
chicken = list()

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(N):
        if temp[j] == 1:
            home.append((i, j))
        elif temp[j] == 2:
            chicken.append((i, j))

temp.clear()

comb = [k for k in range(len(chicken))]
com = list(itertools.combinations(comb, M))


def distance(h, c):
    return abs(h[0]-c[0]) + abs(h[1]-c[1])


# 각 집마다 치킨집 거리
distance_info = [[] for _ in range(len(home))]

for h in range(len(home)):
    for c in chicken:
        distance_info[h].append(distance(home[h], c))


# 폐점된 치킨점을 제외하고 가장 가까운 치킨집 거리의 합 구하고 global 정답 구하기
global_sum = 10000000

for c in com:
    local_sum = 0

    for d in distance_info:
        for o in c:
            temp.append(d[o])
        local_sum += min(temp)
        temp.clear()

    global_sum = min(global_sum, local_sum)


print(global_sum)

