import sys

sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cnt = 0

    def BFS(n, m):
        global cnt
        que = list()
        que.append(n)
        start = 0
        end = 1

        while True:
            cnt += 1
            for i in range(start, end):
                if que[i] + 1 == m or que[i] - 1 == m or que[i] * 2 == m or que[i] - 10 == m :
                    return
                if 0 < que[i] + 1 <= 1000000 and que[i] < m and que[i] + 1 not in que:
                    que.append(que[i]+1)
                if 0 < que[i] - 1 <= 1000000 and que[i] - 1 not in que:
                    que.append(que[i]-1)
                if que[i] < m and 0 < que[i] * 2 <= 1000000 and que[i] * 2 not in que:
                    que.append(que[i]*2)
                if 0 < que[i] - 10 <= 1000000 and que[i] - 10 not in que:
                    que.append(que[i]-10)

            start = end
            end = len(que)

    BFS(N, M)

    print(f'#{tc} {cnt}')

