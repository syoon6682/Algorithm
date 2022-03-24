import sys

sys.stdin = open("input.txt", "r")

T = 10

for tc in range(1, T + 1):
    cnt = int(input())
    height_list = list(map(int, input().split()))
    count_list = [0]*101 # index 100까지 있는 count_list

    for i in height_list:
        count_list[i] += 1 # count_list 채우기

    min_pointer = 0
    max_pointer = 100

    # pointer를 0이 아닌 위치까지 이동시키기
    while True:
        if count_list[min_pointer] == 0:
            min_pointer += 1
        else:
            break

    while True:
        if count_list[max_pointer] == 0:
            max_pointer -= 1
        else:
            break

    # max에서 min으로 덜어주고 그에 따른 pointer와 count_list의 값 변화
    for _ in range(cnt):
        count_list[max_pointer] -= 1
        count_list[max_pointer - 1] += 1
        if count_list[max_pointer] == 0:
            max_pointer -= 1

        count_list[min_pointer] -= 1
        count_list[min_pointer + 1] += 1
        if count_list[min_pointer] == 0:
            min_pointer += 1

        if max_pointer - min_pointer == 0:
            break

    print(f'#{tc} {max_pointer - min_pointer}')

