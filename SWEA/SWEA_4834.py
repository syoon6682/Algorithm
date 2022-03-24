import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, list(input())))
    cnt_list = [0]*10

    for i in range(len(num_list)):
        cnt_list[num_list[i]] += 1

    max_num = 0
    max_cnt = 0
    for j in range(len(cnt_list)):
        if cnt_list[j] >= max_cnt:
            max_num = j
            max_cnt = cnt_list[j]

    print(f'#{tc} {max_num} {max_cnt}')

