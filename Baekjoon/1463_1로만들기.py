from collections import deque

N = int(input())
num = [0] * 1000001
num[1] = 1
visited = deque()
visited.append(1)

while True:
    if num[N] != 0:
        print(num[N]-1)
        break
    else:
        temp = visited[0]
        if temp * 2 <= 1000000 and num[temp*2] == 0:
            num[temp*2] = num[temp] + 1
            visited.append(temp*2)

        if temp * 3 <= 1000000 and num[temp*3] == 0:
            num[temp*3] = num[temp] + 1
            visited.append(temp*3)

        if temp + 1 <= 1000000 and num[temp+1] == 0:
            num[temp+1] = num[temp] + 1
            visited.append(temp+1)

        visited.popleft()



