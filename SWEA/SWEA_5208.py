import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):

    # 데이터 받기
    battery = list(map(int, input().split()))
    N = battery[0]
    cnt = 0

    # drive 함수 정의
    def drive(s):
        global cnt

        # 만약 기준점에서의 베터리만으로 끝까지 갈 수 있으면 끝까지 가고 함수 종료
        if s + battery[s] >= N:
            return

        else:
            cnt += 1                            # 끝까지 못가므로 중간에 들리는 횟수 한번 늘려주고
            max_drive = 0                       # 기준점에서 언제 충전할 때 가장 멀리 갈 수 있는지 알아보자
            for i in range(1, battery[s]+1):
                temp = s + i + battery[s+i]     # temp = 기준점부터 이동 거리 + 도착점에서 더 갈 수 있는 거리인디
                if temp > max_drive:            # 이게 제일 크면 이걸 저장해주면 되겠지
                    max_point = s + i
                    max_drive = temp

            # max point를 기준으로 다시 drive 함수 진행
            drive(max_point)

    drive(1)

    print(f'#{tc} {cnt}')
