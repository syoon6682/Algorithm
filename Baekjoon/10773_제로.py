N = int(input())
sum_list = list()

for _ in range(N):
    n = int(input())
    if n == 0:
        sum_list.pop()
    else:
        sum_list.append(n)

print(sum(sum_list))