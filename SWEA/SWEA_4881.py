import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    map_list = list(list(map(int, input().split())) for _ in range(N))


    def cal(idx, col, N):
        if idx == N:
            print(lst)
            return

        if lst[idx] == 0:
            cal

    lst = [0]*N
    print(f'#{tc} {map_list}')

