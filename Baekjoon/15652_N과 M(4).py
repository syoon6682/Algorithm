N, M = map(int, input().split())
arr = list()


def dfs(n):
    global N
    global M

    if n == M:
        for j in arr:
            print(j, end=' ')
        print()
        return
    else:
        for i in range(1, N+1):
            if n != 0 and i < arr[-1]:
                continue
            arr.append(i)
            dfs(n+1)
            arr.pop()

dfs(0)