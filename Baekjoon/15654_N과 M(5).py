import itertools

N, M = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

arr = list(itertools.permutations(num, M))
for a in arr:
    for i in a:
        print(i, end=' ')
    print()

