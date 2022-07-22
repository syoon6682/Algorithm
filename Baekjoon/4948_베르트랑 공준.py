while True:
    n = int(input())
    if n == 0 :
        break
    else:
        s = n
        e = 2*n
        num_list = [1] * (e+1)

        # 에라토스테네스 체 구현
        for i in range(2, e+1):
            if num_list[i] == 1:
                for j in range(2, (e//i)+1):
                    num_list[i*j] = 0

        # count 구현
        cnt = 0
        for k in range(s+1, e+1):
            if num_list[k] == 1:
                cnt += 1
        print(cnt)
