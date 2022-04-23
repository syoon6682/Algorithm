N = int(input())
num_plus = [0] * 10000001
num_minus = [0] * 10000001

num_list = list(map(int, input().split()))
for n in num_list:
    if n >= 0:
        num_plus[n] += 1
    else:
        num_minus[n] += 1

M = int(input())
search_list = list(map(int, input().split()))
for s in search_list:
    if s >= 0:
        print(num_plus[s], end=' ')
    else:
        print(num_minus[s], end=' ')


