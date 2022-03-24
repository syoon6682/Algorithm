N = int(input())

start = 0
i = 1

while True:
    if start < N <= start+i:
        N = N - start
        i += 1
        break
    else:
        start += i
        i += 1
if i%2 == 1:
    print(f'{N}/{i-N}')

elif i%2 == 0:
    print(f'{i-N}/{N}')
