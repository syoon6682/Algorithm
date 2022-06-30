from collections import deque

A, B = map(int, input().split())


deq = deque()
deq.append(B)
visited = list()
visited.append(B)
def bfs():
    global A
    cnt = 1
    while True:
        if not deq:
            return -1
        else:
            for _ in range(len(deq)):
                temp = deq.popleft()
                if temp % 2 == 0:
                    visited.append(temp // 2)
                    deq.append(temp // 2)

                temp = str(temp)
                if temp[-1] == '1':
                    temp = temp[0:-1]
                    if temp != '':
                        visited.append(int(temp))
                        deq.append(int(temp))

                cnt += 1

                if A in visited:
                    return cnt

print(bfs())