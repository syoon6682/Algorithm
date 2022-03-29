import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    # 데이터 받기 및 visited 함수 생성
    N = int(input())
    num_list = list(list(map(int, input().split())) for _ in range(N))
    visited = [1]
    min_tot = 100000000

    # 이동 경로를 다 짜줄 수 있는 함수
    def routing():
        if len(visited) == N:
            cal(visited)
            return

        else:
            for i in range(2, N+1):
                if i not in visited:
                    visited.append(i)
                    routing()
                    visited.pop()

    # 짜여진 이동 경로를 토대로 계산
    def cal(l):
        global min_tot
        tot = 0
        l.append(1) # 맨 마지막에 도착하게 1 더해주고
        for i in range(N):
            tot += num_list[l[i]-1][l[i+1]-1]
        l.pop() # 다시 원래대로 돌아와주고 (이걸 안하면 백트래킹이 정상적으로 진행이 안됨)
        if tot < min_tot:
            min_tot = tot

    # 만든 함수 돌리기
    routing()

    print(f'#{tc} {min_tot}')

