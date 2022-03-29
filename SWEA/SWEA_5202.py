import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    # 데이터 받기
    N = int(input())

    # [시작시간, 끝시간, 걸리는 시간] 방식으로 list에 저장
    schedule = list()
    for _ in range(N):
        a, b = map(int, input().split())
        schedule.append([a, b, b-a])
    t = 1                                   # 기준 간격 시간
    cnt = 0                                 # 개수
    timeline = [0]*24                       # 시간이 곂치는지 확인할 timeline

    # 시간이 짧게 걸리는 거부터 배치하는 방식으로 진행
    while t < 24: # 걸리는 시간은 24시간을 넘지 않으므로 조건을 이렇게 걸어주기
        for s in schedule:
            if s[2] == t:
                temp = s
                # 중간에 이미 다른 일이 있으면 포기
                for i in range(s[0], s[1]):
                    if timeline[i] == 1:
                        break
                # 없으면 시간표에 채워주고 1 카운트
                else:
                    for i in range(s[0], s[1]):
                        timeline[i] = 1
                    cnt += 1

        t += 1

    print(f'#{tc} {cnt}')

