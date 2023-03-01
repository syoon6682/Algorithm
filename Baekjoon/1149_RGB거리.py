N = int(input())
R = list()
G = list()
B = list()
cost = list()
for _ in range(N):
    temp = list(map(int, input().split()))
    cost.append(temp)

for i in range(N):
    if i == 0:
        R.append(cost[0][0])
        G.append(cost[0][1])
        B.append(cost[0][2])
    else:
        R_new = min(G[-1] + cost[i][0], B[-1] + cost[i][0])
        G_new = min(R[-1] + cost[i][1], B[-1] + cost[i][1])
        B_new = min(R[-1] + cost[i][2], G[-1] + cost[i][2])

        R.append(R_new)
        G.append(G_new)
        B.append(B_new)

print(min(R[-1], G[-1], B[-1]))



