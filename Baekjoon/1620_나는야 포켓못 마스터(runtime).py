N, M = map(int, input().split())

pocketmon = list()

for _ in range(N):
    pocketmon.append(input())

for _ in range(M):
    i = input()
    if i.isdecimal() == 1:
        print(pocketmon[int(i)-1])
    else:
        print(pocketmon.index(i)+1)