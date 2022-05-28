def position(x, y, test):
    len_x = abs(test[0]-x)
    len_y = abs(test[1]-y)

    # 원 밖에 있을 때, 0 반환
    if len_x ** 2 + len_y ** 2 > test[2] ** 2:
        return 0
    # 원 안에 있을 때, 1 반환
    else:
        return 1


T = int(input())

for t in range(T):
    sx, sy, es, ey = map(int, input().split())
    star_num = int(input())
    star_list = []
    for s in range(star_num):
        star_list.append(list(map(int, input().split())))

    cnt = 0
    for star in star_list:
        if position(sx, sy, star) != position(es, ey, star):
            cnt += 1

    print(cnt)