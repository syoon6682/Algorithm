N, M = map(int, input().split())

truth = list(map(int, input().split()))

if len(truth) == 1:
    truth = []
else:
    truth = truth[1:]

truth = set(truth)

party = list()

for _ in range(M):
    party.append(list(map(int, input().split()))[1:])


check = [0] * M

while True:
    flag = False
    for i in range(M):
        if check[i] == 0:
            for j in party[i]:
                if j in truth:
                    flag = True
                    truth.update(party[i])
                    check[i] = 1
    if not flag:
        break

print(check.count(0))



