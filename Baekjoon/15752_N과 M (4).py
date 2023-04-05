N, M = map(int, input().split())

memo = [1] * M
pointer = -1
while True:
    if memo[pointer] > N:
        for i in range(M-1):
            pointer -= 1
            if memo[pointer] < N:
                pass

    else:
        print(memo)
        memo[pointer] += 1


