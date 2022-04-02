import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    node = list(map(int, input().split()))
    E = len(node) // 2
    V = max(node)
    visited = list()
    adjL = [list() for _ in range(V+1)]
    adjM = list([0]*(V+1) for _ in range(V+1))
    for i in range(E):
        n1, n2 = node[i*2], node[i*2+1]
        adjL[n1].append(n2)
        adjL[n2].append(n1)
        adjM[n1][n2] = 1
        adjM[n2][n1] = 1

    def DFS(s):
        visited.append(s)
        for w in range(V+1):
            if adjM[s][w] == 1 and (w not in visited):
                DFS(w)

    DFS(1)



    print(f'#{tc} {visited}')