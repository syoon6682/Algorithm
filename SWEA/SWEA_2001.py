import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    def part_sum(m):
        p_sum = 0
        for k in range(m):
            for l in range(m):
                p_sum += fly_list[i + k][j + l]
        return p_sum

    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            if part_sum(M) > max_sum:
                max_sum = part_sum(M)

    print(f'#{tc} {max_sum}')

