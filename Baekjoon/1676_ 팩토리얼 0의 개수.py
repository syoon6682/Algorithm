N = int(input())

cnt = 0
for i in range(1, N+1):
    if i % 125 == 0:
        cnt += 3
    elif i % 25 == 0:
        cnt += 2
    elif i % 5 == 0:
        cnt += 1

print(cnt)