import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    num_list = list(list(map(int, input().split())) for _ in range(4))

    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def make_num(x, y, idx):
        if idx == 7:
            check(bit)

        else:
            bit[idx] = num_list[x][y]
            for d in delta:
                new_x = x + d[0]
                new_y = y + d[1]
                if new_x >= 4 or new_y >= 4 or new_x < 0 or new_y < 0:
                    continue
                else:
                    make_num(new_x, new_y, idx + 1)

    def check(tester):
        for r in repo:
            if r == tester:
                break
        else:
            repo.append(tester)


    bit = [0]*7
    repo = []
    make_num(0, 0, 0)
    print(len(repo))

    print(f'#{tc} {len(repo)}')

