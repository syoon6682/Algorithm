import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    height = list(list(map(int, input().split())) for _ in range(N))
    cost = list([0]*N for _ in range(N))

    def BFS():
        que = list()
        que.append([0, 0, 0])
        visited = list()
        visited.append([0, 0, 0])
        delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        start = 0
        end = 1
        while start < end:
            for i in range(start, end):




    print(f'#{tc} {cost}')

