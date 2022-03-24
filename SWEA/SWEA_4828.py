import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    list_max = num_list[0]
    list_min = num_list[0]
    for i in num_list:
        if i > list_max:
            list_max = i

        if i < list_min:
            list_min = i

    print(f'#{tc} {list_max - list_min}')

