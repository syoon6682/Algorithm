N, M = map(int, input().split())

board = list([0] * M for _ in range(N))
cnt = 0

arrow = list()
for _ in range(N):
    arrow.append(list(input()))


def forward(x, y):
    while True:
        direc = arrow[x][y]
        if direc == 'D':
            x += 1
        elif direc == 'U':
            x -= 1
        elif direc == 'L':
            y -= 1
        elif direc == 'R':
            y += 1

        if board[x][y] == 1:
            return
        else:
            board[x][y] = 1


def backward(x, y):
    if x-1 >= 0 and board[x-1][y] == 0 and arrow[x-1][y] == "D":
        x = x-1
        board[x][y] = 1
        backward(x, y)
    if x+1 < N and board[x+1][y] == 0 and arrow[x+1][y] == "U":
        x = x+1
        board[x][y] = 1
        backward(x, y)
    if y+1 < M and board[x][y+1] == 0 and arrow[x][y+1] == "L":
        y = y+1
        board[x][y] = 1
        backward(x, y)
    if y-1 >= 0 and board[x][y-1] == 0 and arrow[x][y-1] == "R":
        y = y-1
        board[x][y] = 1
        backward(x, y)


for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            continue
        else:
            board[i][j] = 1
            forward(i, j)
            backward(i, j)
            cnt += 1

print(cnt)
