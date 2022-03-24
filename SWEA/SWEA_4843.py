import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))

    for i in range(len(num_list)):
        if i % 2 == 0: # index가 짝수일 경우
            temp_max = num_list[i]
            temp_point = i
            for j in range(i, len(num_list)): # 남은 범위의 가장 큰 수를 구하는 for문
                if num_list[j] > temp_max:
                    temp_point = j
                    temp_max = num_list[j]
            num_list[i], num_list[temp_point] = num_list[temp_point], num_list[i]

        else: # index가 홀수일 경우
            temp_min = num_list[i]
            temp_point = i
            for j in range(i, len(num_list)): # 남은 범위의 가장 작은 수를 구하는 for문
                if num_list[j] < temp_min:
                    temp_point = j
                    temp_min = num_list[j]
            num_list[i], num_list[temp_point] = num_list[temp_point], num_list[i]

    print(f'#{tc} ', end = '') # 넘버링
    for i in range(len(num_list)): # list 항목을 상위 10개만 나열
        print(num_list[i], end = ' ')
        if i == 9:
            break
    print('')

