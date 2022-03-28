N = int(input())
base = 1
n = 1
while True:
    if N == 1:
        print(1)
        break
    elif N <= base + n*6:
        print(n+1)
        break
    else:
        base += n*6
        n += 1

