import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    rlt = 1

    def line_check(line):
        for std in range(len(line) - 1):
            for search in range(std + 1, len(line)):
                if line[std] == line[search]:
                    return 0
        return 1

    def block_check(init_point_x, init_point_y):
        temp_list = []
        for k in range(3):
            for l in range(3):
                temp_list.append(sudoku[init_point_x + k][init_point_y + l])

        return line_check(temp_list)


    # block check
    x, y = 0, 0
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            rlt *= block_check(x + i, y + j)

    # 가로 체크
    for i in range(9):
        rlt *= line_check(sudoku[i])

    for i in range(9):
        for j in range(9):
            if i > j:
                sudoku[i][j], sudoku[j][i] = sudoku[j][i], sudoku[i][j]

    # 세로 체크
    for i in range(9):
        rlt *= line_check(sudoku[i])

    print(f'#{tc} {rlt}')

