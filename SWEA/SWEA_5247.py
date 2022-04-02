import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cnt = 0

    while N != M:
        temp = [N + 1, N - 1, N * 2, N - 10]
        temp_min = 1000000
        cal = 0
        for t in temp:
            if abs(M - t) < temp_min:
                temp_min = abs(M-t)
                cal = t
        N = cal
        cnt += 1

    print(f'#{tc} {cnt}')

