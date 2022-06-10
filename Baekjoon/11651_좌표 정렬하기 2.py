import sys

N = int(sys.stdin.readline())

locate = list()
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    locate.append([x, y])

locate.sort(key=lambda x:(x[1], x[0]))


for l in locate:
    print(l[0], l[1])

