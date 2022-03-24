import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    test_list = [2, 3, 5, 7, 11]

    print(f'#{tc} ', end='')

    for i in test_list:
        cnt = 0
        while N % i == 0:
            cnt += 1
            N = N // i
        print(cnt, end=' ')

    print('')


