N, M = map(int, input().split())
info = dict()

for _ in range(N):
    site, password = map(str, input().split())
    info[site] = password

for _ in range(M):
    question = input()
    print(info[question])

