chess = list(map(int, input().split()))

std = [1, 1, 2, 2, 2, 8]

for c in range(6):
    print(std[c] - chess[c], end=' ')