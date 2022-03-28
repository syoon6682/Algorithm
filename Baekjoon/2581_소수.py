M = int(input())
N = int(input())

Aratos = [0]*(N+1)
Aratos[0] = 1
Aratos[1] = 1
n = 2
while True:
    for i in range(n,N+1):
        if Aratos[i] == 0:
            cnt = 2
            while i * cnt <= N:
                Aratos[i*cnt] = 1
                cnt += 1
        break

    n = n + 1
    if n ** 2 >= N:
        break

tot_sum = 0
tot_min = 10001
for i in range(M, N+1):
    if Aratos[i] == 0:
        tot_sum += i
        if i < tot_min:
            tot_min = i

if tot_sum > 0:
    print(tot_sum)
    print(tot_min)

else:
    print(-1)
