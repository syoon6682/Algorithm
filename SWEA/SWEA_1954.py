import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    num_list = []
    for i in range(N):
        num_list.append([0] * N) # 0으로 채워진 N * N 2차원 배열 생성

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    input_number = N + 1
    direction = 1
    cnt = N - 1
    point = [0, N-1] # 필요한 델타와 변수들 설정

    for i in range(N):
        num_list[0][i] = i+1

    while cnt > 0:
        for _ in range(2): # 4,4 3,3, 2,2 이런 식으로 2번씩 반복되므로 2번 반복
            for _ in range(cnt):
                num_list[point[0] + dx[direction]][point[1] + dy[direction]] = input_number
                input_number += 1
                point = [point[0] + dx[direction], point[1] + dy[direction]]

            if direction == 3: # direction이 3을 넘으면 다시 0으로 돌아감
                direction = 0
            else:
                direction += 1
        cnt -= 1

# 출력
    print(f'#{tc} ')
    for i in num_list:
        for j in i:
            print(j, end = ' ')
        print('')

