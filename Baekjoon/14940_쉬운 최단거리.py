n, m = map(int, input().split())

maze = list()

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 2:
            temp[j] = 0
            start_x, start_y = i, j
        elif temp[j] == 1:
            temp[j] = -1
        else:
            pass
        
    maze.append(temp)

def bfs(start_x, start_y):
    global n
    global m
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = list()
    visited.append((start_x,start_y))
    cnt = 1
    
    while True:
        new_visited = list()
        for x, y in visited:
            for i in range(4):
                new_x = x+dx[i]
                new_y = y+dy[i]
                
                if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                    continue
                if maze[new_x][new_y] != -1:
                    continue
                maze[new_x][new_y] = cnt
                new_visited.append((new_x, new_y))
        cnt += 1
        
        if not new_visited:
            break
        else:
            visited = new_visited


bfs(start_x, start_y)

for m in maze:
    for t in m:
        print(t, end=' ')
    print()