import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stop_list = list(map(int, input().split())) # 주어진 데이터 입력받기
    stop_list.append(N) # 맨 끝에 목적지의 좌표도 추가
    cnt = 0

    init_position = 0
    while True:
        if stop_list[0] - init_position > K: # 현 시점에서 다음 정류장과의 거리가 최대 이동거리보다 길 경우
            print(f'#{tc} 0')
            break

        elif stop_list[-1] - init_position < K: # 현 시점으로부터 바로 목적지에 도착할 수 있는 경우
            print(f'#{tc} {cnt}')
            break

        else:
            for i in range(0, len(stop_list)): # 그 외의 경우
                if stop_list[i] - init_position > K:
                    init_position = stop_list[i-1]
                    stop_list = stop_list[i::]
                    cnt += 1
                    break

            else:
                print(f'#{tc} {cnt}')
                break



