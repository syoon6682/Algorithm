
N = int(input())

one = [1]
two = []
three = []
four = []
num = [0] * (N+1)

cnt = 0
while True:
    cnt += 1
    temp = one[-1] + cnt * 4 + 1
    if temp <= N:
        one.append(temp)
        num[temp] = 1
    else:
        break

def dp(n):
    # two phase
    for i in range(len(one)):
        for j in range(i, len(one)):
            temp = one[i] + one[j]
            if temp > n:
                continue

            if num[temp] == 0:
                two.append(temp)
                num[temp] = 1
    if num[N] == 1:
        return 2

    # three phase
    for i in one:
        for j in two:
            temp = i + j
            if temp > n:
                continue
            if num[temp] == 0:
                three.append(temp)
                num[temp] = 1
    if num[N] == 1:
        return 3

    # four phase
    for i in one:
        for j in three:
            temp = i + j
            if temp > n:
                continue
            if num[temp] == 0:
                four.append(temp)
                num[temp] = 1
    if num[N] == 1:
        return 4

    # four phase
    for i in two:
        for j in two:
            temp = i + j
            if temp > n:
                continue
            if num[temp] == 0:
                four.append(temp)
                num[temp] = 1
    if num[N] == 1:
        return 4

    return 5



if N == 11 or N == 26:
    print(6)

elif N in one:
    print(1)

else:
    print(dp(N))


