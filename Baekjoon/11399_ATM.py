N = int(input())
num = list(map(int, input().split()))

num.sort()

rlt = 0
for i in range(N):
    rlt += num[i]*(N-i)

print(rlt)