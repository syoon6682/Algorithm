T = int(input())

for _ in range(T):
    H, W, N = map(int,input().split())
    if N % H != 0:
        front = N // H + 1
    else:
        front = N // H

    if front < 10:
        front = '0' + str(front)

    else:
        front = str(front)

    if N % H != 0:
        end = str(N % H)
    else:
        end = str(H)

    print(end + front)
