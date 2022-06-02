import sys

N, M = map(int, input().split())

N_list = list()
M_list = list()
sol_list = list()

for _ in range(N):
    N_list.append(sys.stdin.readline().strip())

for _ in range(M):
    M_list.append(sys.stdin.readline().strip())

N_list.sort()
M_list.sort()


for m in M_list:
    if len(N_list) == 0:
        break
    for n in N_list:
        if n < m:
            N_list.remove(n)

        elif n == m:
            sol_list.append(n)
            N_list.remove(n)
            break

        elif n > m:
            break

for s in sol_list:
    print(s)
