N = int(input())

stair = list()
for _ in range(N):
    stair.append(int(input()))

if len(stair) == 1:
    print(stair[0])
elif len(stair) == 2:
    print(stair[0] + stair[1])
else:
    answer = list()


def dfs(l, s):
    if len(l) == len(stair):
        return
    else:
        if s == 0 or s == 1:
            answer.append(stair[s])
        elif answer[s-1] == answer[s-2]:
            answer.append(answer[s-1] + stair[s])
