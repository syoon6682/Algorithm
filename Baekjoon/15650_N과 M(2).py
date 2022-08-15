N, M = map(int, input().split())
visited = list()


def dfs(n, m, s):
    if s == m:
        for v in visited:
            print(v, end=' ')
        print()
        return

    else:
        for i in range(1, N+1):
            if len(visited) == 0:
                visited.append(i)
                dfs(n, m, s + 1)
                visited.pop()
            elif i not in visited and i > visited[-1]:
                visited.append(i)
                dfs(n, m, s+1)
                visited.pop()


dfs(N, M, 0)