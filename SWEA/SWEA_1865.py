import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):

    # 데이터 받고 가장 큰 확률값을 받는 P_max 함수를 0으로 초기화, visited 함수 생성
    N = int(input())
    work = list(list(map(int, input().split())) for _ in range(N))
    P_max = 0
    visited = list()


    # 확률계산하는 cal_P함수
    def cal_P(idx, tot):
        global P_max

        # 종료조건에 도달하면 P_max에 저장
        if idx == N:
            P_max = tot
            return

        else:
            for i in range(N):
                if i not in visited:        # visited에 들어있지 않으면
                    visited.append(i)       # visited에 기록
                    before = tot            # 전 tot 상태 기록
                    tot *= work[idx][i]     # tot에 해당하는 확률값 곱하기

                    # 얘가 중요한데 tot에 0이 곱해지는 순간 최대값이 될 가능성은 아예 없으므로 가지치기
                    # 그리고 최대 확률 값은 100인데 남은 횟수를 모두 100을 곱해도 최대값이 안되더라도 가지치기하는 조건문
                    if tot > 0 and (100**(N-idx-1))*tot >= P_max:
                        cal_P(idx+1, tot)

                    # 백트레킹 과정인데 전 과정으로 돌리기 위해 아까 저장한 before 쓰는게 매우 중요(1로 초기화했다가 너무 고생했어요..ㅜㅜ)
                    visited.pop()
                    if tot != 0:
                        tot //= work[idx][i]
                    elif tot == 0:
                        tot = before


    cal_P(0, 1)

    # 문제에서 원하는 방식으로 값 변환해주기
    result = P_max / (100 ** N) * 100

    print(f'#{tc} {result:.6f}')

