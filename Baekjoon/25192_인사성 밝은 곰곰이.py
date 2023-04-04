import sys

N = int(sys.stdin.readline())

name = set()
total_cnt = 0
cnt = 0
for _ in range(N):
    temp = sys.stdin.readline()
    if temp == 'ENTER':
        total_cnt += len(name)
        name.clear()
        continue
    name.add(temp)

total_cnt += len(name)

print(total_cnt)