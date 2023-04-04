N, M = map(int, input().split())

basket = [0] * (N+1)

for _ in range(M):
    s, e, n = map(int, input().split())
    for i in range(s, e+1):
        basket[i] = n

for b in range(1, N+1):
    print(basket[b], end=" ")

