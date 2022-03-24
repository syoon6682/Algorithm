import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N, interval = map(int, input().split())
    num_list = list(map(int, input().split()))
    control_point = 0

    for i in range(interval):
        control_point += num_list[i]

    max_sum = control_point
    min_sum = control_point

    for i in range(N - interval + 1):
        total_sum = 0
        for j in range(interval):
            total_sum += num_list[i + j]

        if total_sum > max_sum:
            max_sum = total_sum
        if total_sum < min_sum:
            min_sum = total_sum

    print(f'#{tc} {max_sum - min_sum}')

