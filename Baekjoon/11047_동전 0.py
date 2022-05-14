N, K = map(int, input().split())
cnt = 0
money = []
for _ in range(N):
    money.append(int(input()))

while K != 0:
    target = 0
    for m in range(len(money)):
        if money[m] > K:
            target = money[m-1]
            break
    else:
        target = money[-1]
    K -= target
    cnt += 1

print(cnt)