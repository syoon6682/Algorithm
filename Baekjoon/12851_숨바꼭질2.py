N, K = map(int, input().split())

memo = set()
memo.add(N)
cnt = 1
num = 0
flag = False
visited = [N]

if N == K:
    print(0)
    print(0)
else:

    while True:
        if K + 1 in memo:
            num += 1
            flag = True
        if K - 1 in memo:
            num += 1
            flag = True
        if K % 2 == 0 and K // 2 in memo:
            num += 1
            flag = True
        if flag:
            break

        cnt += 1

        new_visited = visited[:]
        visited.clear()
        for i in range(0, len(new_visited)):
            test = new_visited[i]
            if test+1 <= 200000 and test + 1 not in memo:
                memo.add(test+1)
                visited.append(test+1)
            if test-1 >= 0 and test-1 not in memo:
                memo.add(test-1)
                visited.append(test-1)
            if test*2 <= 200000 and test*2 not in memo:
                memo.add(test*2)
                visited.append(test*2)

    print(cnt)
    print(num)
