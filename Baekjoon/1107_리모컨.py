N = int(input())
M = int(input())
if M != 0:
    broken = list(map(int, input().split()))
else:
    broken = list()


def checker(n):
    n = str(n)
    for s in n:
        if int(s) in broken:
            return False
    return True


if len(broken) == 10:
    print(abs(100 - N))
else:
    if checker(N):
        print(min(abs(100 - N), len(str(N))))
    else:
        up_N = N
        down_N = N
        while True:
            up_N += 1
            if down_N > 0:
                down_N -= 1

            if abs(100-N) < abs(down_N-N):
                print(abs(100-N))
                break

            if checker(down_N):
                print(min(abs(100 - N), len(str(down_N)) + abs(down_N - N)))
                break

            if checker(up_N):
                print(min(abs(100 - N), len(str(up_N)) + abs(up_N - N)))
                break



