from sys import stdin


N, M = map(int, stdin.readline().split())

A = set()
B = list()
for _ in range(N):
    A.add(stdin.readline().strip())

for _ in range(N, N+M):
    B.append(stdin.readline().strip())

intersec = list(A & set(B))


tot = 0
for i in intersec:
    tot += B.count(i)
print(tot)


