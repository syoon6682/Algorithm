import copy

N = int(input())

cnt = 0
board = list([0]*N for _ in range(N))
flag = 0


def marker(a, b):
    global board

    # 해당 점 마킹
    board[a][b] = 1

    # 우하대각 마킹
    x = a
    y = b
    while True:
        x += 1
        y += 1
        if x >= N or y >= N:
            break
        else:
            board[x][y] = 1

    # 좌하대각 마킹
    x = a
    y = b
    while True:
        x += 1
        y -= 1
        if x >= N or y < 0:
            break
        else:
            board[x][y] = 1

    # 하단 마킹
    x = a
    y = b
    while True:
        x += 1
        if x >= N:
            break
        else:
            board[x][y] = 1


def even_dfs(n):
    global cnt
    global board

    if n == N:
        cnt += 2
        return

    target = board[n]

    if 0 not in target:
        return

    else:
        if n == 0:
            for j in range(N//2):
                if target[j] == 0:
                    before_board = [item[:] for item in board]
                    marker(n, j)
                    even_dfs(n+1)
                    board = before_board
        else:
            for j in range(N):
                if target[j] == 0:
                    before_board = [item[:] for item in board]
                    marker(n, j)
                    even_dfs(n+1)
                    board = before_board


def uneven_dfs(n):
    global cnt
    global board
    global flag

    if n == N and flag != N//2:
        cnt += 2
        return
    elif n == N and flag == N//2:
        cnt += 1
        return

    target = board[n]

    if 0 not in target:
        return

    else:
        if n == 0:
            for j in range(N//2 + 1):
                flag = j
                if target[j] == 0:
                    before_board = [item[:] for item in board]
                    marker(n, j)
                    uneven_dfs(n + 1)
                    board = before_board

        else:
            for j in range(N):
                if target[j] == 0:
                    before_board = [item[:] for item in board]
                    marker(n, j)
                    uneven_dfs(n+1)
                    board = before_board


if N == 1:
    print(1)
elif N % 2 == 0:
    even_dfs(0)
    print(cnt)
else:
    uneven_dfs(0)
    print(cnt)


