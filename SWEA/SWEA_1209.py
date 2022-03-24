import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []

    for i in range(100):
        temp_sum = 0
        for j in range(100):
            temp_sum += num_list[i][j]
        sum_list.append(temp_sum) # 가로축 sum

    for j in range(100):
        temp_sum = 0
        for i in range(100):
            temp_sum += num_list[i][j]
        sum_list.append(temp_sum)  # 세로축 sum

    temp_sum = 0
    for i in range(100):
        temp_sum += num_list[i][i]
    sum_list.append(temp_sum) # 좌상 우하 대각선 합

    temp_sum = 0
    for i in range(100):
        temp_sum += num_list[i][99-i]
    sum_list.append(temp_sum) # 우상 좌하 대각선 합

    maximum = 0
    for i in sum_list:
        if i > maximum:
            maximum = i # sum_list의 최대값을 찾는 과정

    print(f'#{tc} ')
    print(maximum)
