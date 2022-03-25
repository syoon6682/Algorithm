import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):

    # board setting
    N, M = map(int, input().split())
    board = list([0]*N for _ in range(N))
    board[N//2][N//2-1], board[N//2-1][N//2] = 1, 1
    board[N//2-1][N//2-1], board[N//2][N//2] = 2, 2

    delta = [(1,-1), (1, 0), (1, 1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

    def searching(x, y, c):
        change = list()
        change.append(c)
        change.append([x, y])
        for d in delta:

            temp = list()
            new_x = x + d[0]
            new_y = y + d[1]

            while True:

                if new_x >= N or new_y >= N or new_x < 0 or new_y < 0:
                    temp = list()
                    break

                elif board[new_x][new_y] == c:
                    break

                elif board[new_x][new_y] == 0:
                    temp = list()
                    break

                elif board[new_x][new_y] != c:
                    temp.append([new_x, new_y])
                    new_x = new_x + d[0]
                    new_y = new_y + d[1]

            change += temp

        return change_point(change)

    def change_point(change):
        change_color = change[0]
        for b in range(1, len(change)):
            board[change[b][0]][change[b][1]] = change_color

    for _ in range(M):
        X, Y, C = map(int, input().split())
        searching(X-1, Y-1, C)

    count_1 = 0
    count_2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                count_1 += 1
            elif board[i][j] == 2:
                count_2 += 1

    print(f'#{tc} {count_1} {count_2}')

