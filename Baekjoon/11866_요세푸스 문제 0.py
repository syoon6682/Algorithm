N, K = map(int, input().split())

num = [1] * N

rlt = list()


def yose(k, pointer):
    global N
    cnt = 0
    while cnt < k:
        if pointer >= N:
            pointer -= N

        elif num[pointer] == 1:
            cnt += 1
            pointer += 1

        else:
            pointer += 1

    num[pointer-1] = 0
    rlt.append(pointer)
    return pointer


point = 0
while len(rlt) < N:
    point = yose(K, point)

# 출력형식 너무 귀찮고~
print('<', end='')
for r in range(len(rlt)-1):
    print(f'{rlt[r]}, ', end='')
print(f'{rlt[-1]}>')

