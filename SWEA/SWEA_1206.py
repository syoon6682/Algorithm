import sys

sys.stdin = open('input.txt', 'r')

T = 10

for tc in range(1, T + 1):
    N = int(sys.stdin.readline())
    build_list = list(map(int, sys.stdin.readline().split()))
    good_view = 0

    for i in range(2, N - 3):
        temp_build_list = [build_list[i-2], build_list[i-1], build_list[i+1], build_list[i+2]]
        temp_build_list = list(map(lambda x : build_list[i] - x, temp_build_list))
        if min(temp_build_list) < 0:
            continue
        else:
            good_view += min(temp_build_list)

    print(f'#{tc} {good_view}')

