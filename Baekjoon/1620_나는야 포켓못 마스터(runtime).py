import sys

N, M = map(int, sys.stdin.readline().split())

pocketmon = list()
answer_list = list()

for _ in range(N):
    pocketmon.append(sys.stdin.readline().strip())


for _ in range(M):
    answer_list.append(sys.stdin.readline().strip())


for a in answer_list:
    if a.isdecimal():
        print(pocketmon[int(a)-1])
    else:
        print(pocketmon.index(a)+1)