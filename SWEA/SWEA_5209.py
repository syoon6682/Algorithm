import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):

    # 데이터 받고 최소값 저장 함수를 큰 값으로 저장
    N = int(input())
    factory = list(list(map(int, input().split())) for _ in range(N))
    visited = []
    tot_min = 10000000

    # 함수 정의를 통해 문제 풀이
    def product(idx, tot):
        global tot_min

        # 종료조건
        if idx == N:
            # tot이 tot_min보다 작으면 tot으로 대체
            if tot < tot_min:
                tot_min = tot
            return

        else:
            for i in range(N):
                if i not in visited:
                    visited.append(i)
                    tot += factory[idx][i]
                    if tot <= tot_min: # 만약 지금까지의 합이 tot_min보다 작으면 진행, 그렇지 않으면 가지치기
                        product(idx + 1, tot)
                    # pop 과정으로 visited 들어가기 전 상황과 똑같이 만들어주기
                    visited.pop()
                    tot -= factory[idx][i]

    product(0, 0)

    print(f'#{tc} {tot_min}')
