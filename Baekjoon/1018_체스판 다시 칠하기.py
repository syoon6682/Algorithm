N, M = map(int, input().split())
w_line = 'WBWBWBWB'
b_line = 'BWBWBWBW'
tot_min = 64
board = []
for _ in range(N):
    temp = input()
    board.append(temp)


def white_board_test(x, y):
    cnt = 0
    for i in range(8):
        s = board[x][y:y+8]
        if i % 2 == 0:
            for j in range(8):
                if w_line[j] != s[j]:
                    cnt += 1
        else:
            for j in range(8):
                if b_line[j] != s[j]:
                    cnt += 1
        x += 1

    return cnt


def black_board_test(x, y):
    cnt = 0
    for i in range(8):
        s = board[x][y:y+8]
        if i % 2 == 1:
            for j in range(8):
                if w_line[j] != s[j]:
                    cnt += 1
        else:
            for j in range(8):
                if b_line[j] != s[j]:
                    cnt += 1
        x += 1

    return cnt


for x in range(N-7):
    for y in range(M-7):
        result = black_board_test(x, y)
        if result < tot_min:
            tot_min = result
        result = white_board_test(x, y)
        if result < tot_min:
            tot_min = result

print(tot_min)