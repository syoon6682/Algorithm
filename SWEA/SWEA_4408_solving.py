import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    std_list = []
    for i in range(N):
        a, b = map(int, input().split())
        if a % 2 == 0:
            a -= 1
        if b % 2 == 1:
            b += 1
        std_list.append([a, b])

    print(std_list)
    print(f'#{tc} ')

