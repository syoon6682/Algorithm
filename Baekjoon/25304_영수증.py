T = int(input())
N = int(input())

tot = 0
for i in range(N):
    n, m = map(int, input().split())
    tot += n*m

if T == tot:
    print('Yes')
else:
    print('No')