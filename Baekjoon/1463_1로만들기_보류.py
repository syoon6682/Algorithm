N = int(input())

cnt = 0
while True:
    if N >= 16 and

    if N % 3 == 0:
        N = N // 3
        cnt += 1
    else:
        N = N - 1
        cnt += 1
    if N == 1:
        break
print(cnt)