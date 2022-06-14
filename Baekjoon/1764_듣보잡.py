import sys

N, M = map(int, input().split())

N_list = list()
M_list = list()
sol_list = list()

for _ in range(N):
    N_list.append(sys.stdin.readline().strip())

for _ in range(M):
    M_list.append(sys.stdin.readline().strip())

N_list = set(N_list)
M_list = set(M_list)

intersection = list(N_list & M_list)
intersection.sort()


print(len(intersection))
for i in intersection:
    print(i)