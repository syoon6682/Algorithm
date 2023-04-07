import pprint
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
status = "row"

def dfs(now, point):
    global cnt
    global status

    if point == (N-1, N-1):
        cnt += 1
        return
    else:
        if now == 'row':
            # 우측 이동
            if point[1]+1 < N and board[point[0]][point[1]+1] != 1:
                status = 'row'
                dfs(status, (point[0], point[1]+1))
                status = now


            # 대각 이동
            if (point[1]+1 < N and point[0]+1 < N
                    and board[point[0]][point[1]+1] != 1
                    and board[point[0]+1][point[1]+1] != 1
                    and board[point[0]+1][point[1]] != 1):
                status = 'diagonal'
                dfs(status, (point[0]+1, point[1]+1))
                status = now

        elif now == 'column':
            # 하단 이동
            if point[0]+1 < N and board[point[0]+1][point[1]] != 1:
                status = 'column'
                dfs(status, (point[0] + 1, point[1]))
                status = now
            # 대각 이동
            if (point[1]+1 < N and point[0]+1 < N
                    and board[point[0]][point[1]+1] != 1
                    and board[point[0]+1][point[1]+1] != 1
                    and board[point[0]+1][point[1]] != 1):
                status = 'diagonal'
                dfs(status, (point[0] + 1, point[1] + 1))
                status = now

        elif now == 'diagonal':
            # 우측 이동
            if point[1] + 1 < N and board[point[0]][point[1] + 1] != 1:
                status = 'row'
                dfs(status, (point[0], point[1] + 1))
                status = now
            # 하단 이동
            if point[0] + 1 < N and board[point[0] + 1][point[1]] != 1:
                status = 'column'
                dfs(status, (point[0] + 1, point[1]))
                status = now
            # 대각 이동
            if (point[1] + 1 < N and point[0] + 1 < N
                    and board[point[0]][point[1] + 1] != 1
                    and board[point[0] + 1][point[1] + 1] != 1
                    and board[point[0] + 1][point[1]] != 1):
                status = 'diagonal'
                dfs(status, (point[0] + 1, point[1] + 1))
                status = now


dfs(status, (0,1))

print(cnt)