N = int(input())
n = int(input())
broken = list()
if n != 0:
    broken = list(map(int, input().split()))
elif n == 0:
    broken = list()

sol = abs(100-N)


def tester(num):
    global N
    num = str(num)
    for s in num:
        if int(s) in broken:
            return False
    return True


if tester(N):
    temp = len(str(N))
    if sol < temp:
        print(sol)
    else:
        print(temp)
else:
    up = N
    down = N
    while True:
        up += 1
        if down > 0:
            down -= 1

        if tester(up):
            temp = len(str(N)) + abs(up-N)
            if sol < temp:
                print(sol)
                break
            else:
                print(temp)
                break

        elif tester(down):
            temp = len(str(N)) + abs(down - N)
            if sol < temp:
                print(sol)
                break
            else:
                print(temp)
                break

        if abs(N - up) > sol:
            print(sol)
            break
