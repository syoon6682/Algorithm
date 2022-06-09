
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    answer = 1

    for i in range(M-N+1, M+1):
        answer *= i

    for j in range(1,N+1):
        answer //= j

    print(answer)