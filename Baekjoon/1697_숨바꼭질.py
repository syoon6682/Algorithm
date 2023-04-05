from collections import deque

N, K = map(int, input().split())
deq = deque()
visited = list()
deq.append(N)
visited.append(N)
cnt = 0
while True:
    if K in visited:
        break

    for _ in range(len(deq)):
        test = deq.popleft()

        visited.append(test-1)
        deq.append(test-1)

        visited.append(test+1)
        deq.append(test+1)

        visited.append(test*2)
        deq.append(test*2)
    cnt += 1


print(cnt)
