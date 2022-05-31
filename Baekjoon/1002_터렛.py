from math import sqrt

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    interval = (abs(x1 - x2) ** 2) + (abs(y1 - y2) ** 2)
    tester = (r1 + r2) ** 2

    # 서로 똑같은 경우
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)

    # 원 안에 존재하는 경우
    elif interval < r1 ** 2 or interval < r2 ** 2:
        r_max = max(r1, r2)
        r_min = min(r1, r2)
        interval_sqrt = sqrt(interval)

        if interval_sqrt + r_min < r_max:
            print(0)
        elif interval_sqrt + r_min == r_max:
            print(1)
        else:
            print(2)

    # 원 위에 존재하는 경우
    elif interval == r1 ** 2 or interval == r2 ** 2:
        print(2)

    # 서로 원 밖에 있는 경우
    elif interval > r1 ** 2 and interval > r2 ** 2:
        if interval < tester:
            print(2)
        elif interval == tester:
            print(1)
        else:
            print(0)
