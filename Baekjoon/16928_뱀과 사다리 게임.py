from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())

ladder = dict()

for _ in range(N+M):
    a, b = map(int, stdin.readline().split())
    ladder[a] = b


visited = deque()
visited.append(1)
def bfs():
    cnt = 0
    while True:
        if 100 in visited:
            print(cnt)
            break
        else:
            end = len(visited)
            for i in range(end):
                point = visited[0]
                for d in range(1, 7):
                    test = point + d
                    if test > 100:
                        continue
                    else:
                        if ladder.get(test) != None:
                            test = ladder[test]
                        if test not in visited:
                            visited.append(test)
                visited.popleft()
            cnt += 1

bfs()
