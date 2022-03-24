'''
일단 아무리 봐도 모범답안은 아닌 거 같네요..
재귀적인 호출은 구현이 잘 안되서 stack 추가와 백트레킹을 한번에 하는 함수를 정의한 후
조건에 만족할 때까지 계속 방복하는 방법으로 코드를 짰습니다.
'''

import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    # 데이터 N과 2차원 배열 받기

    N = int(input())
    map_list = []
    for i in range(N): # 숫자 사이에 공간이 없어서 문자로 받아버린 후 하나씩 다시 list로 입력
        temp_list = []
        temp_S = input()
        for j in range(len(temp_S)):
            temp_list.append(int(temp_S[j]))
            if temp_S[j] == '2':
                init_point = [i, j]
        map_list.append(temp_list)

    stack = [init_point] # 시작점을 넣어두고 stack 생성
    check_map = [[0]*N for _ in range(N)] # 경로를 갔는지 체크하는 지도 체크 리스트 (갔으면 1, 안갔으면 0)
    check_map[init_point[0]][init_point[1]] = 1 # 첫 시작점은 1 찍기

    def push_stack():

        if len(stack) == 0: # 스택이 비어있으면 false를 반환
            return 'false'

        d = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 사방 탐색

        for dx, dy in d: # 좌표 반영
            modified_x = stack[-1][0] + dx
            modified_y = stack[-1][1] + dy

            # 범위 벗어나면 넘어가기
            if modified_x < 0 or modified_y < 0 or modified_x >= N or modified_y >= N:
                continue

            # 도착점 찾으면 찾았다고 외치기
            elif map_list[modified_x][modified_y] == 3:
                return 'find'

            # 갔던 길이면 쳐다도 안보기
            elif check_map[modified_x][modified_y] == 1:
                continue

            # 갈 수 있는 길이면 stack에 추가하고 갔다고 표시한 다음 더 시도
            elif map_list[modified_x][modified_y] == 0:
                stack.append([modified_x, modified_y])
                check_map[modified_x][modified_y] = 1
                return 'more try'

            # 현재의 위치에서 아무 곳도 갈 수 없으면 그 전 경로에서 새로 탐색
        else:
            if len(stack) != 0:
                stack.pop()
                return 'more try'

    while True: # 될 때까지 반복
        result = push_stack()
        if result == 'find': # 찾으면 1 반환
            print(f'#{tc} 1')
            break
        elif result == 'false': # 못찾으면 0 반환
            print(f'#{tc} 0')
            break

