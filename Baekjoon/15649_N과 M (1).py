N, M = map(int, input().split())
visited = []


def printer(check):
    global N, M

    # 전체 숫자 리스트
    num_list = list(range(1, N+1))

    if len(visited) == M:
        for v in visited:
            print(v, end=' ')
        print()
        return
    else:
        for i in num_list:
            if i not in visited:
                visited.append(i)
                printer(check+1)
                visited.remove(i)


printer(0)



