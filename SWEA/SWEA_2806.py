import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    # 데이터 받기
    N = int(input())
    board = list([0] * N for _ in range(N))
    cnt = 0

    # 1을 찾는 queen 함수 정의
    def queen(idx, n):
        global cnt
        if idx == N:
            cnt += 1
            return
        else:
            for i in range(N):
                if block_test(idx, i):
                    board[idx][i] = 1
                    queen(idx+1, n)
                    board[idx][i] = 0

    # 임의의 자리에 queen을 두었을때 범위에 다른 queen이 있는지 판단하는 함수
    def block_test(x, y):

        # 대각선까지 가능하므로 대각선도 반영한 delta 설정
        delta = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        if board[x][y] != 0:
            return 0

        # 각 델타 끝까지 검사해보기
        for d in delta:
            new_x = x
            new_y = y
            while True:
                new_x += d[0]
                new_y += d[1]
                if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N: # 범위를 벗어나면 break
                    break
                elif board[new_x][new_y] == 1:
                    return 0

        return 1

    queen(0, N)

    print(f'#{tc} {cnt}')

