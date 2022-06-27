n, m = map(int, input().split())

N, M = 1, 1

answer = 1
for i in range(m):
    answer *= (n-i)

for i in range(m):
    answer //= (i+1)

print(answer)
