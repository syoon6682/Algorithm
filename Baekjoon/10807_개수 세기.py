N = int(input())
integer = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in integer:
    if i == v:
        cnt += 1

print(cnt)

