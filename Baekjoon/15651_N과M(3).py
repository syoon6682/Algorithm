N, M = map(int, input().split())
store = list()

def dfs(m):
    global N
    global M

    if m == M:
        for s in store:
            print(s, end=' ')
        print()
        return
    else:
        for i in range(1, N+1):
            store.append(i)
            dfs(m+1)
            store.pop()

dfs(0)