T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    pattern = list()
    temp = 1
    for i in range(1, 11):
        temp *= a
        temp = temp % 10
        if temp not in pattern:
            pattern.append(temp)
        else:
            break
    if a % 10 == 0:
        print(10)
    else:
        print(pattern[b % len(pattern)-1])