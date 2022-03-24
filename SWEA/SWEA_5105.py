import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    map_list = []

    # 공백이 없어서 문자로 받고 2차원 배열 만들기
    for i in range(N):
        temp = input()
        temp_list = []
        for s in temp:
            temp_list.append(int(s))
        map_list.append(temp_list)

    # 시작점 찾기
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == 2:
                start = [i, j]
                break

    # delta 설정
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # queue 생성 후 시작 포인트 추가
    Queue = list()
    Queue.append(start)
    start = 0
    end = 1
    cnt = 0

    # 경로 판별
    def routing(queue):
        for pts in range(start, end):
            point = [queue[pts][0], queue[pts][1]]
            # 델타 설정
            for d in delta:
                new_point = [point[0]+d[0], point[1]+d[1]]

                # 갔던 길을 가는 경우
                try:
                    if queue.index([new_point[0], new_point[1]]) == int:
                        continue
                except ValueError:

                    # 가장자리에 부딪히는 경우
                    if new_point[0] >= N or new_point[1] >= N or new_point[0] < 0 or new_point[1] < 0:
                        continue

                    # 1에 부딪히는 경우
                    elif map_list[new_point[0]][new_point[1]] == 1:
                        continue

                    # 도착지에 도착한 경우 거리 측정
                    elif map_list[new_point[0]][new_point[1]] == 3:
                        return cnt

                    # 길이 있는 경우 queue에 현재 위치 추가
                    elif map_list[new_point[0]][new_point[1]] == 0:
                        queue.append(new_point)

        # 모든 경우를 다한 경우
        return 'replay'

    while True:
        result = routing(Queue)
        # 아직 도착 못했을 경우
        if result == 'replay':
            start = end
            end = len(Queue)
            cnt += 1

            # Queue의 시작점과 끝점이 만나면 도착이 안되는 구조이므로 0 출력
            if start == end:
                result = 0
                break
        else:
            break

    print(f'#{tc} {result}')

