T = int(input())

# 0 <= n <= 10000 범위의 에라토스테네스체 구현
prime = [1] * 10001
for j in range(2, 10001):
    if prime[j] == 1:
        k = 2
        while j * k <= 10000:
            prime[j*k] = 0
            k += 1

for i in range(T):
    n = int(input())
    a = n//2
    b = n//2
    while True:
        if (prime[a] == 1) and (prime[b] == 1):
            print(a, b)
            break
        else:
            a -= 1
            b += 1
