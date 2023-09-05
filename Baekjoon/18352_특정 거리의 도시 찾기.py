from collections import deque

N, M, K, X = map(int, input().split())

road = list([] * (N+1) for _ in range(N+1))

for i in range(M):
    s, e = map(int, input().split())
    road[s].append(e)
    
city_memo = set()
city_memo.add(X)

queue = deque([X])

def bfs():
    global K
    cnt = 0
    while True:
        cnt += 1
        temp = list(queue)
        for i in temp:
            for j in road[i]:
                if j not in city_memo:
                    city_memo.add(j)
                    queue.append(j)
            queue.popleft()
        
        if cnt == K:
            return list(queue)

result = bfs()

if not result: 
    print(-1)
else:
    for k in sorted(result):
        print(k)