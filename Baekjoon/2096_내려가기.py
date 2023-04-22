N = int(input())

one_max = 0
two_max = 0
three_max = 0

one_min = 0
two_min = 0
three_min = 0

for i in range(N):
    a, b, c = map(int, input().split())

    if i == 0:
        one_max, one_min = a, a
        two_max, two_min = b, b
        three_max, three_min = c, c

    else:
        one_tmax = max(one_max+a, two_max+a)
        two_tmax = max(one_max+b, two_max+b, three_max+b)
        three_tmax = max(two_max+c, three_max+c)

        one_tmin = min(one_min+a, two_min+a)
        two_tmin = min(one_min+b, two_min+b, three_min+b)
        three_tmin = min(two_min+c, three_min+c)

        one_max, one_min = one_tmax, one_tmin
        two_max, two_min = two_tmax, two_tmin
        three_max, three_min = three_tmax, three_tmin

print(max(one_max, two_max, three_max), min(one_min, two_min, three_min))