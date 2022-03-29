import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    # 데이터와 2차원 visited 생성
    N = int(input())
    num_list = list(list(map(int, input().split())) for _ in range(N))
    visited = list([0] * N for _ in range(N))
    min_sum = 10000000

    # 길 찾는 routing 함수
    def routing(x, y, tot): # 파라미터 추가(지금까지의 sum) -> 이러면 중간중간 비교가 가능!
        global min_sum
        # 추가적인 종료조건
        # 중간중간에서 (현 위치에서의) sum 비교
        # 이때 중간인데도 min_sum 보다 크다면 걸러야지

        # 종료조건
        tot += num_list[x][y]

        if x == N - 1 and y == N - 1:
            visited[x][y] = 1
            if tot < min_sum:
                min_sum = tot
            return

        if tot > min_sum:
            return

        else:
            if x < N - 1:
                visited[x][y] = 1
                routing(x + 1, y, tot)
                visited[x][y] = 0 # stack에서 pop의 개념으로 활용

            if y < N - 1:
                visited[x][y] = 1
                routing(x, y + 1, tot)
                visited[x][y] = 0

    routing(0, 0, 0)


    print(f'#{tc} {min_sum}')

